drop table if exists qads.clima;

create table if not exists qads.clima
(
	clima_id         Integer auto_increment not null primary key,
	ponto_id         Integer                not null,
	dt_referencia    Timestamp              not null,
	lat              Double                 null,
	lon              Double                 null,
	precipitacao_mm  Double                 null,
	pressao_mb       Double                 null,
	umidade_relativa Double                 null,
	temperatura_k    Double                 null,
	vento_ms         Double                 null,

	index clima_ponto_id_dt ( ponto_id, dt_referencia ),
	index clima_dt ( dt_referencia )
)
;

drop table if exists resumo_clima;
create table resumo_clima as (

                             with
	                             pontos_coleta as (
	                             select
		                             row_number( ) over () as ponto_id
	                               , t.*
		                             from
			                             (
			                             select distinct
				                             lat
			                               , lon
				                             from
					                             clima
			                             ) t
	                             )

                               , distances as (
                                              select
	                                              aero.id_aerodromo
	                                            , aero.nm_municipio
	                                            , ponto.ponto_id
	                                            , ponto.lat
	                                            , ponto.lon
	                                            , acos(
				                                              cos( radians( aero.lat ) )
				                                              * cos( radians( ponto.lat ) )
				                                              * cos( radians( aero.lon ) - radians( ponto.lon ) )
			                                              + sin( radians( aero.lat ) )
					                                              * sin( radians( ponto.lat ) )
		                                              ) * 6371 as dist_km
	                                              from
		                                              nrm_aeroporto aero
		                                            , pontos_coleta ponto
	                                              where
		                                                aero.lon is not null
		                                            and aero.lat is not null
		                                            and ponto.lat is not null
		                                            and ponto.lon is not null
		                                            and aero.nm_municipio in ( 'SÃO PAULO', 'RIO DE JANEIRO' )
                                              )

                               , aero_ponto_coleta as (
                                                      select *
	                                                      from
		                                                      (
		                                                      select
			                                                      row_number( ) over ( partition by id_aerodromo order by dist_km) as ranking
			                                                    , distances.*
			                                                      from
				                                                      distances
		                                                      ) t
	                                                      where
		                                                      ranking = 1
                                                      )

                             select
	                             nm_municipio
                               , date( dt_referencia )      as dt_referencia
                               , sum( precipitacao_mm )     as precipitacao_mm
                               , avg( pressao_mb )          as pressao_mb
                               , avg( umidade_relativa )    as umidade_relativa
                               , avg( temperatura_k ) + 273 as temperatura_k
                               , avg( vento_ms )            as vento_ms
	                             from
		                             clima
		                             inner join aero_ponto_coleta apc on clima.ponto_id = apc.ponto_id
	                             group by
		                             nm_municipio
	                               , date( dt_referencia )
                             );



select
	nm_municipio
  , dt_referencia + interval 1 day as dt_referencia
  , precipitacao_mm
  , pressao_mb
  , umidade_relativa
  , temperatura_k
  , vento_ms
	from
		resumo_clima;


call pc_optimize_tables_like( 'qads', '%', '%' )