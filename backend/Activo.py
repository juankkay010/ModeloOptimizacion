import yfinance as yf
import pandas as pd
from tabulate import tabulate


class Activo:
    def __init__(self, nombre, simbolo):
        self.nombre = nombre
        self.simbolo = simbolo
        self.open = None
        self.high = None
        self.low = None
        self.close = None
        self.adj_close = None
        self.volume = None

    def descargar_datos(self, periodo):
        info_activo = yf.Ticker(self.simbolo)
        historia_activo = info_activo.history(period=periodo)
        self.open = historia_activo['Open']
        self.high = historia_activo['High']
        self.low = historia_activo['Low']
        self.close = historia_activo['Close']
        #self.adj_close = historia_activo['adjclose']
        self.volume = historia_activo['Volume']

    def tabla_informacion_activo(self):
        df_concatenado = pd.concat([self.open, self.high, self.low, self.close, self.volume], axis=1)
        return tabulate(df_concatenado, headers=["Date", "Open", "High", "Low", "Close", "Volume"])




