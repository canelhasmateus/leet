import io
import re

import pandas as pd
import requests
from bs4 import BeautifulSoup
from tqdm import tqdm
import database
import voos
import zipfile

JANUARY = 1
DECEMBER = 13

END_YEAR = 2021
INITIAL_YEAR = 2015

ERRORS = [ ]
voos_url = voos.voos_url


# region stale
def estatisticos():
	# vars = "https://www.gov.br/anac/pt-br/assuntos/dados-e-estatisticas/descricao-de-variaveis"
	urls = [ ]
	for ano in range( INITIAL_YEAR, END_YEAR ):
		url = f"https://www.gov.br/anac/pt-br/assuntos/dados-e-estatisticas/dados-estatisticos/arquivos/resumo_anual_{ano}.csv"
		urls.append( url )

	def download_estatisticos( url ):
		df = pd.read_csv( url, encoding = "latin1", sep = ";" )
		df.to_sql( "estatisticos", database.engine, "qads", if_exists = "append" )

	action = retry( 2, download_estatisticos )
	for url in tqdm( urls, "estatisticos" ):
		action( url )


def atrasos():
	urls = [
			"https://www.anac.gov.br/acesso-a-informacao/dados-abertos/areas-de-atuacao/voos-e-operacoes-aereas/percentuais-de-atrasos-e-cancelamentos/voos-e-operacoes-aereas-anexo-ii-percentuais-de"
			"-atrasos-e-de-cancelamentos-de-voos-consolidados-por-empresa-e-por-par-de-aeroportos-de-origem-e-de-destino" ]

	def download_atrasos( url ):
		df = pd.read_csv( url, sep = ";" )
		df.to_sql( "atrasos", database.engine, "qads", if_exists = "append" )

	action = retry( 2, download_atrasos )
	for url in tqdm( urls ):
		action( url )


# endregion

# region help

def retry( num, f ):
	def wrappped( *args, **kwargs ):

		for i in range( num ):
			try:
				return f( *args, **kwargs )
			except Exception as e:
				message = f"Error during {f.__name__}: {e} ; \n args: {args} , kwargs: {kwargs}"
				print( message )
				ERRORS.append( message )

	return wrappped


def save_empresa( df ):
	empresa = df[ [ "id_empresa", "nm_empresa",
	                "sg_empresa_icao", "sg_empresa_iata",
	                "sg_empresa_iata", "nm_pais", "ds_tipo_empresa" ] ]
	empresa.drop_duplicates( keep = "first", inplace = True )
	empresa.to_sql( "tmp_micro_empresa", database.engine, "qads", if_exists = "append", index = False )


def save_linha( df ):
	linha = df[ [ "id_tipo_linha",
	              "cd_tipo_linha",
	              "ds_tipo_linha", "ds_natureza_tipo_linha",
	              "ds_servico_tipo_linha",
	              "sg_icao_origem",
	              "sg_icao_destino",
	              "id_aerodromo_origem", "id_aerodromo_destino" ] ]
	linha.drop_duplicates( keep = "first", inplace = True )
	linha.to_sql( "tmp_micro_linha", database.engine, "qads", if_exists = "append", index = False )


def save_etapa( basica_or_combinada, df ):
	id = "id_basica" if basica_or_combinada == "basica" else "id_combinada"
	df[ "dh_partida_real" ] = pd.to_datetime( df[ "dt_partida_real" ] + " " + df[ "hr_partida_real" ], format = "%Y-%m-%d %H:%M:%S" )
	df[ "dh_chegada_real" ] = pd.to_datetime( df[ "dt_chegada_real" ] + " " + df[ "hr_chegada_real" ], format = "%Y-%m-%d %H:%M:%S" )
	columns = [ id, "nr_voo", "nr_singular", "id_di", "id_empresa", "id_tipo_linha", "nr_etapa", "nr_escala_destino", "ds_natureza_etapa", "dt_referencia", "dt_sistema", "dh_partida_real",
	            "dh_chegada_real", "nr_escala_destino", "nr_passag_pagos", "nr_passag_gratis", "kg_bagagem_livre", "kg_bagagem_excesso", "kg_carga_paga", "kg_carga_gratis", "kg_correio"
	            ]
	others = [ "lt_combustivel", "nr_rtk", "nr_velocidade_media", "nr_assentos_ofertados", "nr_pax_gratis_km",
	           "id_equipamento", "nr_carga_gratis_km",
	           "nr_carga_paga_km", "km_distancia", "nr_decolagem", "nr_ask", "nr_atk",
	           "nr_horas_voadas", "kg_payload", "kg_peso", "nr_rpk", "nr_bagagem_gratis_km",
	           "nr_carga_gratis_km", "nr_bagagem_paga_km"
	           ]

	if basica_or_combinada == "basica":
		columns.extend( others )
	etapas = df[ columns ]
	etapas.to_sql( f"tmp_micro_etapa_{basica_or_combinada}", database.engine, "qads", if_exists = "append", chunksize = 10000, index = False )


def save_di( df ):
	di = df[ [ "id_di", "cd_di", "ds_di", "ds_grupo_di" ] ]
	di.drop_duplicates( keep = "first", inplace = True )
	di.to_sql( "tmp_micro_di", database.engine, "qads", if_exists = "append", index = False )


def save_equipamento( df ):
	equipamento = df[ [ "id_equipamento", "sg_equipamento_icao", "ds_modelo", "ds_matricula" ] ]
	equipamento.drop_duplicates( keep = "first", inplace = True )
	equipamento.to_sql( "tmp_micro_equipamento", database.engine, "qads", if_exists = "append", index = False )


def save_aeroporto( df ):
	aeroportos_origem = df[ [ "id_aerodromo_origem", "sg_icao_origem", "sg_iata_origem", "nm_aerodromo_origem", "nm_municipio_origem" ] ]
	aeroportos_destino = df[ [ "id_aerodromo_destino", "sg_icao_destino", "sg_iata_destino", "nm_aerodromo_destino", "nm_municipio_destino" ] ]

	new_columns = [ "id_aerodromo", "sg_icao", "sg_iata", "nm_aerodromo", "nm_municipio" ]
	aeroportos_destino.columns = new_columns
	aeroportos_origem.columns = new_columns

	aero = pd.concat( (aeroportos_destino, aeroportos_origem), axis = 0 ).drop_duplicates( keep = "first" )
	aero.to_sql( "tmp_micro_aeroportos", database.engine, "qads", if_exists = "append", index = False )


def save_etapa_basica( df ):
	save_etapa( "basica", df )


def save_etapa_combinada( df ):
	save_etapa( "combinada", df )


# endregion


def tarifas():
	urls = [ ]
	for year in (2012, 2021):
		for month in (1, 12 + 1):
			month = str( month ) if month >= 10 else "0" + str( month )
			url = f"https://sistemas.anac.gov.br/sas/tarifadomestica/{year}/{year}{month}.csv"
			urls.append( url )

	def download_tarifas( url ):
		df = pd.read_csv( url, sep = ";" )
		df.rename( {
				"EMPRESA" : "nm_empresa",
				"ORIGEM"  : "nm_origem",
				"DESTINO" : "nm_destino",
				"TARIFA"  : "vl_tarifa",
				"ASSENTOS": "nr_assentos",
				}, axis = 1, inplace = True )
		df[ "dt_tarifa" ] = pd.to_datetime( df[ "ANO" ].astype( str ) + "-" + df[ "MES" ].astype( str ), format = "%Y-%m" )
		df.drop( [ "MES", "ANO" ], axis = 1, inplace = True )
		df.to_sql( "tmp-tarifa", database.engine, "qads", if_exists = "append", index = False )

	action = retry( 2, download_tarifas )
	for url in tqdm( urls, "tarifas" ):
		action( url )


def aeroportos():
	urls = [
			"https://sistemas.anac.gov.br/dadosabertos/Aerodromos/Lista%20de%20aer%C3%B3dromos%20p%C3%BAblicos/AerodromosPublicos.csv",
			"https://sistemas.anac.gov.br/dadosabertos/Aerodromos/Lista%20de%20aer%C3%B3dromos%20privados/Aerodromos%20Privados/AerodromosPrivados.csv",
			]

	def download_aeroportos( url ):
		df = pd.read_csv( url, skiprows = 1, sep = ";", encoding = "latin1" )
		df.rename( {
				"Código OACI"      : 'sg_oaci',
				"CIAD"             : 'sg_ciad',
				"Nome"             : "nm_aeroporto",
				"Município"        : "nm_municipio",
				"UF"               : "sg_uf",
				"Município Servido": "nm_municipio_servido",
				"UF Servido"       : "nm_uf_servido",
				"LATGEOPOINT"      : "lat",
				"LONGEOPOINT"      : "lon",
				"Altitude"         : "vl_altitude",
				"Comprimento 1"    : "vl_comprimento",
				"Largura 1"        : "vl_largura"
				}, axis = 1, inplace = True )
		try:
			df = df[ [ 'sg_oaci', 'sg_ciad', 'nm_aeroporto', 'nm_municipio',
			           'sg_uf', 'nm_municipio_servido', 'nm_uf_servido',
			           'lat', 'lon', 'vl_altitude', 'vl_comprimento', 'vl_largura' ] ]


		except Exception as e:
			df = df[ [ 'sg_oaci', 'sg_ciad', 'nm_aeroporto', 'nm_municipio',
			           'sg_uf',
			           'lat', 'lon', 'vl_altitude', 'vl_comprimento', 'vl_largura' ] ]

		df.to_sql( "tmp_aeroporto", database.engine, "qads", if_exists = "append", index = False )

	action = retry( 2, download_aeroportos )
	for url in tqdm( urls, "tmp-aeroportos" ):
		action( url )


def microdados_basicos():
	# vars = "https://www.gov.br/anac/pt-br/assuntos/regulados/empresas-aereas/envio-de-informacoes/descricao-de-variaveis"
	urls = [ ]
	for year in range( INITIAL_YEAR, END_YEAR ):
		for month in range( JANUARY, DECEMBER ):
			month = str( month ) if month >= 10 else "0" + str( month )
			url = f"https://www.gov.br/anac/pt-br/assuntos/regulados/empresas-aereas/envio-de-informacoes/microdados/basica{year}-{month}.zip"
			urls.append( url )

	def download_microdados_basicos( url ):

		df = pd.read_csv( url, encoding = "latin1", sep = ";" )

		save_aeroporto( df )
		save_empresa( df )
		save_linha( df )
		save_equipamento( df )
		save_di( df )
		save_etapa_basica( df )

	action = retry( 2, download_microdados_basicos )

	for url in tqdm( urls, "microdados basicos" ):
		action( url )


def microdados_combinados():
	# vars = "https://www.gov.br/anac/pt-br/assuntos/regulados/empresas-aereas/envio-de-informacoes/descricao-de-variaveis"
	urls = [ ]
	for year in range( INITIAL_YEAR, END_YEAR ):
		for month in range( JANUARY, DECEMBER ):
			month = str( month ) if month >= 10 else "0" + str( month )
			url = f"https://www.gov.br/anac/pt-br/assuntos/regulados/empresas-aereas/envio-de-informacoes/microdados/combinada{year}-{month}.zip"
			urls.append( url )

	def download_microdados_combinados( url ):
		df = pd.read_csv( url, encoding = "latin1", sep = ";" )
		save_aeroporto( df )
		save_empresa( df )
		save_linha( df )

		save_di( df )
		save_etapa_combinada( df )

	action = retry( 2, download_microdados_combinados )
	for url in tqdm( urls, "microdados combinados" ):
		action( url )


def voos():
	# urls = [ ]
	# base_url = "https://sistemas.anac.gov.br/dadosabertos/Voos%20e%20opera%C3%A7%C3%B5es%20a%C3%A9reas/Voo%20Regular%20Ativo%20%28VRA%29/"
	# response = requests.get( base_url ).content.decode( "utf8" )
	# years = [ i.attrs[ "href" ] for i in BeautifulSoup( response, 'html.parser' ).select( "a" ) ]
	# years = [ i for i in years if i != "../" ]
	# for year in years:
	# 	if int( year[ :4 ] ) < 2014:
	# 		continue
	# 	response_year = requests.get( base_url + year ).content.decode( "utf8" )
	# 	months = [ i.attrs[ "href" ] for i in BeautifulSoup( response_year, 'html.parser' ).select( "a" ) ]
	# 	months = [ i for i in months if i != "../" ]
	# 	for month in months:
	# 		response_month = requests.get( base_url + year + month ).content.decode()
	# 		data = [ i.attrs[ "href" ] for i in BeautifulSoup( response_month, 'html.parser' ).select( "a" ) ]
	# 		data = [ i for i in data if str( i ).endswith( ".csv" ) ]
	# 		for fim in data:
	# 			url = base_url + year + month + fim
	# 			urls.append( url )
	urls = voos_url

	def download_voos( url ):
		df = pd.read_csv( url, skiprows = 1, sep = ";" )
		columns = [ "ICAO Empresa Aérea",
		            "Número Voo",
		            "Código Autorização (DI)",
		            "Código Tipo Linha",
		            "ICAO Aeródromo Origem",
		            "ICAO Aeródromo Destino",
		            "Partida Prevista",
		            "Partida Real",
		            "Chegada Prevista",
		            "Chegada Real",
		            "Situação Voo" ]
		df = df[ columns ]

		df = df.rename( {
				"Chegada Real"           : "dt_chegada_real",
				"Chegada Prevista"       : "dt_chegada_prevista",
				"Partida Prevista"       : "dt_partida_prevista",
				"Partida Real"           : "dt_partida_real",
				"ICAO Aeródromo Destino" : "sg_icao_destino",
				"ICAO Aeródromo Origem"  : "sg_icao_origem",
				"Código Tipo Linha"      : "cd_tipo_linha",
				"Código Autorização (DI)": "cd_di",
				"ICAO Empresa Aérea"     : "icao_empresa",
				"Situação Voo"           : "nm_situacao_voo",
				"Número Voo"             : "nr_voo"
				}, axis = 1 )

		# municipios = [ "SÃO PAULO", "RIO DE JANEIRO" ]
		tipos = [ "N", "E", "R" ]
		dis = [ "0", "4", "C" ]
		situacoes = [ "REALIZADO" ]

		# df = df.query( "sg_icao_destino in @municipios" )
		# df = df.query( "sg_icao_origem in @municipios" )
		df = df.query( "cd_tipo_linha in @tipos" )
		df = df.query( "cd_di in @dis" )
		df = df.query( "nm_situacao_voo in @situacoes" )

		for data in [ "dt_chegada_real", "dt_chegada_prevista", "dt_partida_prevista", "dt_partida_real", ]:
			df[ data ] = pd.to_datetime( df[ data ], infer_datetime_format = True )

		df.to_sql( "tmp_voo", database.engine, "qads",
				if_exists = "append",
				chunksize = 10000, index = False )

	action = retry( 2, download_voos )
	for url in tqdm( urls, "voos.py" ):
		action( url )


coleta_ids = { }
global_id = 1


def get_coleta_id( latlon ):
	global global_id
	id = coleta_ids.get( latlon, None )
	if id is None:
		global_id += 1
		id = global_id
		coleta_ids[ latlon ] = id

	return id


def add_id( lat, lon ):
	return coleta_ids.get( (lat, lon), id + 1 )


def clima():
	urls_antiga_formatacao = [ ]
	urls = [ ]
	# headers = { 'content-type': '*/* ; charset=latin1' }

	for year in range( INITIAL_YEAR, END_YEAR ):
		url = f"https://portal.inmet.gov.br/uploads/dadoshistoricos/{year}.zip"
		urls.append( url )

	for url in tqdm( urls ):
		response = requests.get( url )
		archive = zipfile.ZipFile( io.BytesIO( response.content ) )
		paths = [ i for i in archive.namelist() if ('INMET_SE_SP' in i or 'INMET_SE_RJ' in i) ]
		for path in tqdm( paths ):
			csv_bytes = archive.read( path )
			lat, lon, alt = csv_bytes.decode( 'latin1' ).split( '\n' )[ 4:7 ]
			_, lat = lat.split( ";" )
			_, lon = lon.split( ';' )
			_, alt = alt.split( ';' )
			lat = float( lat.replace( ',', '.' ) )
			lon = float( lon.replace( ',', '.' ) )
			alt = float( alt.replace( ',', '.' ) )

			df = pd.read_csv( io.BytesIO( csv_bytes ),
					encoding = 'latin1', skiprows = 8, sep = ';',
					)
			df[ "lat" ], df[ "lon" ], df[ "alt" ] = lat, lon, alt
			df[ "latlon" ] = str( df[ "lat" ] ) + str( df[ "lon" ] )
			df[ "ponto_id" ] = df[ "latlon" ].apply( get_coleta_id )
			df = df.drop( "latlon", axis = 1 )

			renames_numericos = {
					"PRECIPITAÇÃO TOTAL, HORÁRIO (mm)"                     : 'precipitacao_mm',
					"PRESSAO ATMOSFERICA AO NIVEL DA ESTACAO, HORARIA (mB)": 'pressao_mb',
					"UMIDADE RELATIVA DO AR, HORARIA (%)"                  : 'umidade_relativa',
					"TEMPERATURA DO AR - BULBO SECO, HORARIA (°C)"         : 'temperatura_k',
					"VENTO, VELOCIDADE HORARIA (m/s)"                      : 'vento_ms',
					}
			df = df.rename( renames_numericos, axis = 1 )
			numericos = list( renames_numericos.values() )
			for numerico in numericos:
				df[ numerico ] = df[ numerico ].apply( lambda x: float( str( x ).replace( ',', '.' ) ) )
				df[ numerico ] = df[ numerico ].apply( lambda x: pd.NA if x < 0 else x )

			df = df.rename( {
					"DATA (YYYY-MM-DD)": 'DATA',
					"Data"             : 'DATA',
					"HORA (UTC)"       : "HORA",
					"Hora UTC"         : "HORA"
					}, axis = 1 )

			df[ "HORA" ] = df[ "HORA" ].apply( lambda x: re.sub( "[A-Za-z]+", '', x ) )
			df[ 'dt_referencia' ] = pd.to_datetime( df[ "DATA" ] + ' ' + df[ 'HORA' ], infer_datetime_format = True )

			df[ "dt_referencia" ] = df[ "dt_referencia" ] - pd.Timedelta( '3 hour' )

			columns = [ 'dt_referencia', 'ponto_id', 'lat', 'lon' ] + numericos

			df = df[ columns ]

			df.to_sql( 'clima', database.engine,
					schema = 'qads', if_exists = 'append',
					index = False, chunksize = 10000 )


todos = [ voos ]

if __name__ == '__main__':
	for action in tqdm( todos, "all" ):
		action()
