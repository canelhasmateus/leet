import pandas as pd
import numpy as np

from model import encoder, logistic
import logging, time
import weather
# verifica_feriado

from datetime import datetime, timedelta
from telegram import ReplyKeyboardMarkup, ReplyKeyboardRemove, Update, InlineKeyboardMarkup, InlineKeyboardButton
from telegram.ext import (
	Updater,
	CommandHandler,
	MessageHandler,
	Filters,
	ConversationHandler,
	CallbackContext,
	CallbackQueryHandler,
	)

state = { }
logging.basicConfig( format = '%(asctime)s - %(name)s - %(levelname)s - %(message)s', level = logging.INFO )

logger = logging.getLogger( __name__ )

CIDADE, DATA, PREVISAO = range( 3 )


def start( update: Update, context: CallbackContext ):
	reply_keyboard = [ [ '1. São Paulo', '2. Rio de Janeiro' ] ]

	update.message.reply_text(
			'Olá, seja bem vindo à prova de conceito do bot de previsão do atraso de vôos!\n'
			'Envie /cancel para parar de usar o bot.\n\n'
			'Selecione sua cidade de partida:',
			reply_markup = ReplyKeyboardMarkup( reply_keyboard, one_time_keyboard = True,
					input_field_placeholder = 'São Paulo ou Rio de Janeiro?' ) )

	return CIDADE


def cidade( update: Update, context: CallbackContext ):
	cidade = update.message.text

	user = update.message.from_user
	dias_no_futuro = 7
	hoje = datetime.today()
	lista_datas = [ (hoje + timedelta( days = i )).strftime( '%d/%m/%Y' ) for i in range( dias_no_futuro ) ]

	update.message.reply_text(
			f"Seu vôo sairá de {cidade[ 3: ]} em qual data? \n\nSelecione uma data:",
			reply_markup = build_keyboard( lista_datas ) )

	estados = state.get( user, [ ] )
	estados.append( cidade[ 3: ] )
	state[ user ] = estados

	return DATA


def button( update: Update, context: CallbackContext ):
	query = update.callback_query
	user = query.from_user
	data_selecionada = pd.to_datetime( query.data, format = "%d/%m/%Y" )
	data_fmt = data_selecionada.strftime( '%d/%m/%Y' )
	query.edit_message_text( text = f"Selecionado: {data_fmt}" )
	time.sleep( 1 )

	query.edit_message_text( text = f"Obtendo a previsão do tempo...\n" )
	origem = state[ user ][ -1 ]
	clima: weather.OpenWeatherResponse = weather.request_all( origem )
	time.sleep( 3 )

	query.edit_message_text( text = f"Analisando a data informada...\n" )
	dia_semana = data_selecionada.dayofweek
	semana_ano = data_selecionada.week
	destino = "SÃO PAULO" if origem == "RIO DE JANEIRO" else "RIO DE JANEIRO"
	columns = [ 'precipitacao_mm', 'pressao_mb', 'umidade_relativa', 'temperatura_k',
	            'vento_ms', 'sg_empresa_icao', 'municipio_origem', 'municipio_destino',
	            'dia_semana', 'semana_ano', ]
	linhas = [
			[ 40, clima.pressure, clima.humidity, clima.temperature, clima.wind_speed, "AZU", origem, destino, dia_semana, semana_ano ],
			[ 40, clima.pressure, clima.humidity, clima.temperature, clima.wind_speed, "TAM", origem, destino, dia_semana, semana_ano ],
			[ 40, clima.pressure, clima.humidity, clima.temperature, clima.wind_speed, "GLO", origem, destino, dia_semana, semana_ano ],
			]
	df = pd.DataFrame( linhas, columns = columns )
	time.sleep( 3 )
	query.edit_message_text( text = f"Calculando a probabilidade de atraso...\n\n" )
	time.sleep( 3 )

	x = encoder.transform( df )
	probs = logistic.predict_proba( x )[ :, 1 ]
	probs_str = f'AZUL: {np.round(probs[0]*100, 2)} %\nTAM: {np.round(probs[1]*100, 2)} %\nGOL: {np.round(probs[2]*100, 2)} %'
	query.edit_message_text( text = f"As probabilidades de atraso da linha {origem.title()} - {destino.title()} para a data {data_fmt} são: \n{probs_str}" )
	return -1


def build_keyboard( lista_datas: list ) -> InlineKeyboardMarkup:
	keyboard = [ ]
	for data in lista_datas:
		keyboard.append( [ InlineKeyboardButton( data, callback_data = data ) ] )
	return InlineKeyboardMarkup( keyboard, one_time_keyboard = True )


def avalia_clima( update: Update, context: CallbackContext ):
	data = update.message.text

	update.message.reply_text( f"Previsão do tempo para {data}" )


def cancel( update: Update, context: CallbackContext ) -> int:
	"""Cancels and ends the conversation."""
	user = update.message.from_user
	logger.info( "User %s canceled the conversation.", user.first_name )
	update.message.reply_text(
			'Bye! I hope we can talk again some day.', reply_markup = ReplyKeyboardRemove()
			)


def main() -> None:
	updater = Updater( token, use_context = True )

	dispatcher = updater.dispatcher

	conv_handler = ConversationHandler(
			entry_points = [ CommandHandler( 'start', start ) ],
			states = {
					CIDADE: [ MessageHandler( Filters.regex( '^(1|2).+$' ), cidade ) ],
					# PREVISAO: [ CallbackQueryHandler( avalia_clima ) ]
					},
			fallbacks = [ CommandHandler( 'cancel', cancel ) ] )

	dispatcher.add_handler( conv_handler )
	dispatcher.add_handler( CallbackQueryHandler( button ) )

	updater.start_polling()
	updater.idle()


if __name__ == '__main__':
	main()

# TODO
# - Verificar se a data informada é um feriado
# - Verificar a previsao do tempo para a data informada
# - Coletar as informações necessárias para o predict
# - Rodar o modelo para ter o predict para cada companhia
# - Enviar o resultado para o usuário
