import pickle

import matplotlib.pyplot as plt
import pandas as pd
from category_encoders import TargetEncoder
from sklearn.calibration import calibration_curve
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import plot_roc_curve, confusion_matrix, ConfusionMatrixDisplay
from sklearn.model_selection import train_test_split
import pathlib
import database


def treina_modelo():
	voos = pd.read_sql( '''
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

SELECT *
	FROM
		resumo_voos
''', database.engine )
	clima = pd.read_sql( """
select
	nm_municipio
  , dt_referencia + interval 1 day as dt_referencia
  , precipitacao_mm
  , pressao_mb
  , umidade_relativa
  , temperatura_k
  , vento_ms
	from
		resumo_clima
                    """, database.engine )
	for column in voos.columns:
		if column.startswith( "dt" ):
			voos[ column ] = pd.to_datetime( voos[ column ], infer_datetime_format = True )
	for column in clima.columns:
		if column.startswith( "dt" ):
			clima[ column ] = pd.to_datetime( clima[ column ], infer_datetime_format = True )
	voos = voos.query( "atrasado > -60" )
	voos[ "atrasado" ] = voos[ "atrasado" ] >= 20

	df = voos.merge( clima, how = "left",
			left_on = [ "municipio_origem", "dt_referencia" ],
			right_on = [ "nm_municipio", "dt_referencia" ] )
	df[ "dia_semana" ] = df[ "dt_referencia" ].dt.dayofweek
	df[ "semana_ano" ] = df[ "dt_referencia" ].dt.weekofyear
	numericas = [ "precipitacao_mm", "pressao_mb", "umidade_relativa", "temperatura_k", "vento_ms" ]
	categoricas = [ "sg_empresa_icao",
	                "municipio_origem",
	                "municipio_destino",
	                "dia_semana",
	                "semana_ano" ]
	columns_keep = [ ]
	columns_keep.extend( numericas )
	columns_keep.extend( categoricas )
	columns_keep.append( "atrasado" )
	columns_keep.append( "dt_referencia" )
	df = df[ columns_keep ]
	df = (df
	      .sort_values( "dt_referencia" )
	      .groupby( "municipio_origem", as_index = False )
	      .fillna( method = "ffill" )
	      .dropna())

	# numericas_mean = [ i + "_mean" for i in numericas ]
	# numericas_std = [ i + "_std" for i in numericas ]
	# df[ numericas_mean ] = df[ numericas + [ "municipio_origem" ] ].groupby( "municipio_origem" ).transform( pd.Series.mean )
	# df[ numericas_std ] = df[ numericas + [ "municipio_origem" ] ].groupby( "municipio_origem" ).transform( pd.Series.std )
	# for n, m, s in zip( numericas, numericas_mean, numericas_std ):
	# 	df[ n ] = (df[ n ] - df[ m ]) / df[ s ]
	# 	df = df.drop( [ m, s ], axis = 1 )

	df_y = df[ [ "atrasado" ] ]
	df_x = df[ columns_keep ].drop( [ "atrasado", "dt_referencia" ], axis = 1 )
	(df_train_x, df_test_x,
	 df_train_y, df_test_y) = train_test_split( df_x, df_y,
			train_size = 0.8,
			stratify = df_y )
	encoder = TargetEncoder( cols = categoricas,
			handle_unknown = 'value' ).fit( df_train_x, df_train_y )
	df_train_x = encoder.transform( df_train_x )
	df_test_x = encoder.transform( df_test_x )

	forest: RandomForestClassifier = RandomForestClassifier( max_depth = 4, random_state = 1, )
	forest: RandomForestClassifier = forest.fit( df_train_x, df_train_y )
	df_train_yhat_forest = forest.predict_proba( df_train_x )[ :, [ 1 ] ]
	df_test_yhat_forest = forest.predict_proba( df_test_x )[ :, [ 1 ] ]
	logistic: LogisticRegression = LogisticRegression()
	logistic = logistic.fit( df_train_x, df_train_y )
	df_train_yhat_logistic = logistic.predict_proba( df_train_x )[ :, [ 1 ] ]
	df_test_yhat_logistic = logistic.predict_proba( df_test_x )[ :, [ 1 ] ]
	# fig, ax = plt.subplots()
	# ax.plot( [ 0, 1 ], [ 0, 1 ] )
	# plot_roc_curve( forest, df_train_x, df_train_y, ax = ax )
	# plot_roc_curve( logistic, df_train_x, df_train_y, ax = ax )
	# plt.show()
	# cal_train = calibration_curve( df_train_y, df_train_yhat_forest )
	# cal_test = calibration_curve( df_test_y, df_test_yhat_forest )
	# fig, ax = plt.subplots()
	# ax.plot( [ 0, 1 ], [ 0, 1 ] )
	# ax.plot( *cal_train )
	# ax.plot( *cal_test )
	# plt.show()
	# TODO  2021-11-28 hyper-parameter search
	for threshold in range( 70, 100 ):
		threshold = threshold / 100
		y_true = df_train_y
		y_pred = df_train_yhat_logistic >= threshold
		normalize = 'all'
		cm = confusion_matrix(
				y_true,
				y_pred,
				normalize = normalize,
				)
		loss = 10 * cm[ 0, 0 ] + 10 * cm[ 0, 1 ] + 1000 * cm[ 1, 0 ] + 100 * cm[ 1, 1 ]
		print( f"loss : {loss} , threshold: {threshold} " )
		predictions = ConfusionMatrixDisplay.from_predictions( y_true = y_true, y_pred = y_pred,
				normalize = normalize, cmap = 'Blues' )
		plt.show()

	return encoder, logistic


model_path = "./logistic.pickle"
model_file = pathlib.Path( model_path )

encoder_path = "./encoder.pickle"
encoder_file = pathlib.Path( encoder_path )

if not model_file.exists() or not encoder_file.exists():
	encoder, logistic = treina_modelo()
	pickle.dump( logistic, open( model_path, "wb" ) )
	pickle.dump( encoder, open( encoder_path, "wb" ) )
else:
	logistic = pickle.load( open( model_path, "rb" ) )
	encoder = pickle.load( open( encoder_path, "rb" ) )

if __name__ == '__main__':
    treina_modelo()