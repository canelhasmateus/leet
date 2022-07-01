drop table if exists nrm_aeroporto;
create table nrm_aeroporto as (

                              with
	                              aeros as (
	                              select distinct *
		                              from
			                              tmp_micro_aeroportos micro
		                              where
			                                id_aerodromo is not null
		                                and id_aerodromo <> 0

	                              )

                              select distinct
	                              id_aerodromo
                                , sg_oaci
                                , nm_aerodromo
                                , rich.nm_municipio
                                , rich.lat
                                , rich.lon
                                , vl_altitude
                                , vl_comprimento
                                , vl_largura
	                              from
		                              aeros
		                              left join tmp_aeroporto rich on ( rich.sg_oaci = aeros.sg_icao or rich.sg_ciad )
	                              order by
		                              id_aerodromo
                              );
alter table nrm_aeroporto
	add primary key pk_nrm_aerop ( id_aerodromo ),
	row_format compressed;
alter table qads.nrm_aeroporto
	add fulltext index nrm_ft_aero ( nm_aerodromo );
alter table qads.nrm_aeroporto
	add fulltext index nrm_ft_muni ( nm_municipio );

drop table if exists nrm_micro_di;
create table if not exists nrm_micro_di as
	(
	select distinct
		id_di
	  , cd_di
	  , ds_di
	  , ds_grupo_di
		from
			tmp_micro_di
		order by
			id_di
	);
alter table nrm_micro_di
	row_format compressed;

drop table if exists nrm_micro_empresa;
create table if not exists nrm_micro_empresa as
	(
	select distinct *
		from
			tmp_micro_empresa
		order by
			id_empresa
	);
alter table nrm_micro_empresa
	row_format compressed;


drop table if exists nrm_micro_equipamento;
create table if not exists nrm_micro_equipamento as
	(
	select distinct
		id_equipamento
	  , sg_equipamento_icao
	  , ds_modelo
	  , ds_matricula
		from
			tmp_micro_equipamento
		order by
			id_equipamento
	);
alter table nrm_micro_equipamento
	row_format compressed;


drop table if exists nrm_micro_linha;
create table if not exists nrm_micro_linha as
	(
	select distinct
		id_tipo_linha
	  , cd_tipo_linha
	  , ds_tipo_linha
	  , ds_natureza_tipo_linha
	  , ds_servico_tipo_linha
	  , sg_icao_origem
	  , sg_icao_destino
		from
			tmp_micro_linha
		order by
			id_tipo_linha
	);
alter table nrm_micro_linha
	add primary key ( id_tipo_linha ),
	row_format compressed;



drop table if exists nrm_tarifa;
create table if not exists nrm_tarifa as
	(
	select
		tarifa_id
	  , origem.id_aerodromo    as aeroporto_origem_id
	  , destino.id_aerodromo   as aeroporto_destino_id
	  , nrm_empresa.id_empresa as id_empresa
	  , dt_tarifa
	  , vl_tarifa
	  , nr_assentos

# 		     , tarifa.nm_origem
# 		  , tarifa.nm_destino
# 		  , tarifa.nm_empresa

		from
			tmp_tarifa               tarifa
			inner join nrm_aeroporto origem on tarifa.nm_origem = origem.sg_oaci
			inner join nrm_aeroporto destino on tarifa.nm_destino = destino.sg_oaci
			inner join nrm_empresa on tarifa.nm_empresa = nrm_empresa.sg_empresa_icao

	);
alter table nrm_tarifa
	row_format compressed;

drop table if exists nrm_voo;
create table nrm_voo as (
                        select
	                        voo.`número voo`              as nr_voo
                          , voo.`código autorização (di)` as sg_di
                          , voo.`código tipo linha`       as id_tipo_linha

                          , case
	                            when regexp_like( voo.`partida prevista`, '[0-9]{2}/[0-9]{2}/[0-9]{4} [0-9]{2}:[0-9]{2}' )
		                            then str_to_date( voo.`partida prevista`, '%d/%m/%Y %H:%i' )
	                            when regexp_like( voo.`partida prevista`, '[0-9]{4}-[0-9]{2}-[0-9]{2} [0-9]{2}:[0-9]{2}:([0-9]{2})?' )
		                            then str_to_date( voo.`partida prevista`, '%Y-%m-%d %H:%i:%s' )
                            end                           as dt_partida_prevista
                          , case
	                            when regexp_like( voo.`partida real`, '[0-9]{2}/[0-9]{2}/[0-9]{4} [0-9]{2}:[0-9]{2}' )
		                            then str_to_date( voo.`partida real`, '%d/%m/%Y %H:%i' )
	                            when regexp_like( voo.`partida real`, '[0-9]{4}-[0-9]{2}-[0-9]{2} [0-9]{2}:[0-9]{2}:([0-9]{2})?' )
		                            then str_to_date( voo.`partida real`, '%Y-%m-%d %H:%i:%s' )
                            end                           as dt_partida_real
                          , case
	                            when regexp_like( voo.`chegada prevista`, '[0-9]{2}/[0-9]{2}/[0-9]{4} [0-9]{2}:[0-9]{2}' )
		                            then str_to_date( voo.`chegada prevista`, '%d/%m/%Y %H:%i' )
	                            when regexp_like( voo.`chegada prevista`, '[0-9]{4}-[0-9]{2}-[0-9]{2} [0-9]{2}:[0-9]{2}:([0-9]{2})?' )
		                            then str_to_date( voo.`chegada prevista`, '%Y-%m-%d %H:%i:%s' )
                            end                           as dt_chegada_prevista
                          , case
	                            when regexp_like( voo.`chegada real`, '[0-9]{2}/[0-9]{2}/[0-9]{4} [0-9]{2}:[0-9]{2}' )
		                            then str_to_date( voo.`chegada real`, '%d/%m/%Y %H:%i' )
	                            when regexp_like( voo.`chegada real`, '[0-9]{4}-[0-9]{2}-[0-9]{2} [0-9]{2}:[0-9]{2}:([0-9]{2})?' )
		                            then str_to_date( voo.`chegada real`, '%Y-%m-%d %H:%i:%s' )
                            end                           as dt_chegada_real
                          , voo.`situação voo`            as nm_situacao_voo
                          , voo.`código justificativa`    as id_justificativa
                          , empresa.id_empresa
                          , destino.id_aerodromo          as id_aerodromo_destino
                          , origem.id_aerodromo           as id_aerodromo_origem
	                        from
		                        tmp_voos                 voo
		                        inner join nrm_empresa   empresa
		                                   on voo.`icao empresa aérea` = empresa.sg_empresa_icao
		                        inner join nrm_aeroporto destino on voo.`icao aeródromo destino` = destino.sg_oaci
		                        inner join nrm_aeroporto origem on voo.`icao aeródromo origem` = origem.sg_oaci
                        );
alter table nrm_voo
	add index nrm_voo_aero_origem_destino ( id_aerodromo_origem, id_aerodromo_destino ),
	add index nrm_voo_aero_origem ( id_aerodromo_origem ),
	add index nrm_voo_aero_destino ( id_aerodromo_destino ),
	row_format compressed;


drop table if exists tmp_micro_aeroportos;
drop table if exists tmp_micro_di;
drop table if exists tmp_micro_empresa;
drop table if exists tmp_micro_equipamento;
drop table if exists tmp_micro_linha;

create table if not exists qads.voos_sp_sj
(
	voo_id               Integer    not null auto_increment primary key,
	nr_voo               Integer    not null,
	sg_di                Varchar(8) not null,
	id_tipo_linha        Varchar(8) not null,
	dt_partida_prevista  Timestamp  not null,
	dt_partida_real      Timestamp  not null,
	dt_chegada_prevista  Timestamp  not null,
	dt_chegada_real      Timestamp  not null,
	id_empresa           Integer    not null,
	id_aerodromo_destino Integer    not null,
	id_aerodromo_origem  Integer    not null,
	atrasado             Integer    not null,
	atrasado_previsao_1  Integer    not null default 0,
	atrasado_previsao_2  Integer    null,

	index idx_sp_rj_dt_partida ( dt_partida_prevista ),
	index idx_sp_rj_dt_origem ( id_aerodromo_origem ),
	index idx_sp_rj_dt_destino ( id_aerodromo_destino ),
	index idx_sp_rj_emp_origem_fim ( id_empresa, id_aerodromo_origem, id_aerodromo_destino )

) row_format compressed;

insert into
	qads.voos_sp_sj(
	                 nr_voo
	               , sg_di
	               , id_tipo_linha
	               , dt_partida_prevista
	               , dt_partida_real
	               , dt_chegada_prevista
	               , dt_chegada_real
	               , id_empresa
	               , id_aerodromo_destino
	               , id_aerodromo_origem
	               , atrasado
	               , atrasado_previsao_1
	               , atrasado_previsao_2 ) (
	                                       select
		                                       nr_voo
	                                         , sg_di
	                                         , id_tipo_linha
	                                         , dt_partida_prevista
	                                         , dt_partida_real
	                                         , dt_chegada_prevista
	                                         , dt_chegada_real
	                                         , id_empresa
	                                         , id_aerodromo_destino
	                                         , id_aerodromo_origem
	                                         , timestampdiff( minute, voos_sp_sj.dt_chegada_real,
	                                                          voos_sp_sj.dt_chegada_prevista ) >= 20 as atrasado
	                                         , 0                                                     as atrasado_previsao_1
	                                         , 0                                                     as atrasado_previsao_2
		                                       from
			                                       qads.nrm_voo             voos
			                                       inner join nrm_aeroporto origens on origens.id_aerodromo = voos.id_aerodromo_origem
			                                       inner join nrm_aeroporto destinos on destinos.id_aerodromo = voos.id_aerodromo_destino
		                                       where
			                                         voos.id_tipo_linha in ( 'N', 'E', 'R' )
		                                         and voos.sg_di in ( '0', '4', 'C' )
			                                     and origens.nm_municipio in ( 'SÃO PAULO', 'RIO DE JANEIRO' )
			                                     and destinos.nm_municipio in ( 'SÃO PAULO', 'RIO DE JANEIRO' )
			                                     and voos.nm_situacao_voo = 'REALIZADO'
			                                     and dt_partida_prevista is not null
			                                     and dt_partida_real is not null
			                                     and dt_chegada_prevista is not null
			                                     and dt_chegada_real is not null
	                                       );



call pc_optimize_tables_like( 'qads', 'voos_sp_sj', '%' );