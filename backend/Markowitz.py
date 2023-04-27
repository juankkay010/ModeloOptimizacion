import pandas as pd
import numpy as np
from backend.Cartera import *


class Markowitz:
    def __init__(self, cartera):
        self.cartera = cartera

    def calcular_rentabilidad_diaria(self):
        rentabilidad_por_activo = {}
        for simbolo, activo in self.cartera.activos.items():
            rentabilidad_por_activo[simbolo] = activo.adj_close.pct_change()
        return pd.DataFrame(rentabilidad_por_activo)

    def calcular_rentabilidad_promedio(self):
        rentabilidad_diaria = self.calcular_rentabilidad_diaria()
        rentabilidad_promedio = rentabilidad_diaria.mean()
        return rentabilidad_promedio

    def calcular_rentabilidad_cartera_de_inversion(self):
        rentabilidad_promedio = self.calcular_rentabilidad_promedio().values
        porcentajes = [0, 0.2, 0.4, 0.6, 0.8, 1]
        activo1 = rentabilidad_promedio[0]*0.01
        activo2 = rentabilidad_promedio[1]*0.01
        resultado = []
        for i in range(len(porcentajes)-1, -1, -1):
            porcentaje_1 = activo1*porcentajes[i]
            porcentaje_2 = activo2*(100-porcentajes[i])
            resultado.append(porcentaje_2+porcentaje_1)
        return pd.DataFrame(resultado)

    def calcular_varianza(self):
        varianza_por_activo = []
        for activo in self.cartera.activos.values():
            varianza_por_activo.append(activo.adj_close.var()*0.01)
        return varianza_por_activo

    def calcular_matriz_covarianza(self):
        dc_precio_activos = {}
        dc_simbolo_activos = []
        for simbolo, activo in self.cartera.activos.items():
            dc_precio_activos[simbolo] = activo.adj_close
        dt = pd.DataFrame(dc_precio_activos)
        matriz_covarianza = dt.cov()
        for simbolo in self.cartera.activos.keys():
            dc_simbolo_activos.append(simbolo)
        return matriz_covarianza.loc[dc_simbolo_activos[0], dc_simbolo_activos[1]]*0.01

    def calcular_riesgo_cartera_de_inversion(self):
        covarianza = self.calcular_matriz_covarianza()
        varianza = self.calcular_varianza()
        porcentajes = [0, 0.2, 0.4, 0.6, 0.8, 1]
        activo1 = varianza[0]*0.01
        activo2 = varianza[1]*0.01
        resultado = []
        for i in range(len(porcentajes)-1, -1, -1):
            suma_ponderada1 = activo1*porcentajes[i]**2
            suma_ponderada2 = activo2*((100-porcentajes[i])**2)
            suma_covarianza = 2*porcentajes[i]*(100-porcentajes[i])*covarianza
            resultado.append((suma_ponderada1+suma_ponderada2+suma_covarianza)*0.1)
        return pd.DataFrame(resultado)