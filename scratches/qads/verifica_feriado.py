import pandas as pd
import numpy as np
from datetime import datetime, timedelta


def verifica_feriados(data_selecionada):
    feriados = pd.read_csv('feriados.csv', sep=';', encoding='latin1', skiprows=1)
    feriados['Data'] = pd.to_datetime(feriados['Data'], format='%d/%m/%Y')
    feriados.dropna(inplace=True)
    data_selecionada = datetime.strptime(data_selecionada, '%d/%m/%Y')
    print((np.abs(data_selecionada - feriados['Data']) <= timedelta(days=3)).astype(int).sum())

verifica_feriados('20/11/2021')