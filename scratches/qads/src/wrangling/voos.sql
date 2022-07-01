create table resumo_voos as (
                            with
	                            n_vo as (
	                            select
		                            dt_partida_prevista  as dt_referencia
	                              , dt_chegada_real
	                              , dt_chegada_prevista
	                              , icao_empresa         as sg_empresa_icao
	                              , origem.nm_municipio  as municipio_origem
	                              , destino.nm_municipio as municipio_destino
		                            from
			                            tmp_voo                  voos
			                            inner join nrm_aeroporto origem on voos.sg_icao_origem = origem.sg_oaci
			                            inner join nrm_aeroporto destino on voos.sg_icao_origem = origem.sg_oaci
		                            order by
			                            dt_partida_prevista
	                            )
                            SELECT *
	                            FROM
		                            n_vo
                            )
;

select * from tmp_voo;





with
	resumo_voos as (
	select
		date(dt_partida_prevista)  as dt_referencia
	  , dt_chegada_real
	  , dt_chegada_prevista
	  , sg_empresa_icao
	  , origem.nm_municipio  as municipio_origem
	  , destino.nm_municipio as municipio_destino
	  , timestampdiff( minute ,    dt_chegada_prevista , dt_chegada_real ) as atrasado
		from
			voos_sp_sj               voos
			inner join nrm_empresa   empresa on empresa.id_empresa = voos.id_empresa
			inner join nrm_aeroporto origem on origem.id_aerodromo = voos.id_aerodromo_origem
			inner join nrm_aeroporto destino on destino.id_aerodromo = voos.id_aerodromo_destino
		where
				dt_partida_prevista >= '2014-12-30 00:00:00'
		order by
			dt_partida_prevista
	)

select * from resumo_voos;