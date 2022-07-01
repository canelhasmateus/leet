import typing

import pandas as pd


# importing requests and json
import requests, json


class OpenWeatherResponse:
	wind_speed: float
	temperature: float
	max_temperature: float
	min_temperature: float
	min_temperature: float
	pressure : float
	humidity: float

	def __init__( self, weather ):
		self.wind_speed = weather[ "wind" ][ "speed" ]
		self.temperature = weather[ "main" ][ "temp" ]
		self.max_temperature = weather[ "main" ][ "temp_min" ]
		self.min_temperature = weather[ "main" ][ "temp_max" ]
		self.pressure = weather[ "main" ][ "pressure" ]
		self.humidity = weather[ "main" ][ "humidity" ]



def retry( num, f ):
	def wrappped( *args, **kwargs ):

		for i in range( num ):
			try:
				return f( *args, **kwargs )
			except Exception as e:
				message = "Error during: ", f.__name__, ". ", e, "args:", args, ". kwargs: ", kwargs

	return wrappped


def request_weather( city_name: str ) -> typing.Dict:
	query_parameters = {
			"q"    : city_name,
			"appid": API_KEY
			}

	response = requests.get( TEMPERATURE_URL, params = query_parameters )
	if response.status_code != 200:
		raise Exception( "" )
	return response.json()


def request_all( city_name: str ) -> OpenWeatherResponse:
	get_weather = retry( 2, request_weather )

	weather = get_weather( city_name )

	return OpenWeatherResponse( weather )


if __name__ == '__main__':
	response = request_all( "Ipatinga" )

# TODO
# Adicionar preciptacao acumulada
# http://history.openweathermap.org/data/2.5/history/accumulated_precipitation?q={city name}&start={start}&end={end}&appid={API key}
# https://openweathermap.org/api/accumulated-parameters#precip



# Preprocessamento ->
#     TargetEncoder
#     Standardization por cidade.

# Thresholding ->
#     Qual o threshold que escolhemos para considerar que o voo irá atrasar?
#     Isso caso a gente vá retornar 'classe positiva ou negativa' para o usuário.


