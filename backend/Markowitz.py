import pandas as pd
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
        porcentajes = [0, 20, 40, 60, 80, 100]
        activo1 = rentabilidad_promedio[0]*0.01
        activo2 = rentabilidad_promedio[1]*0.01
        resultado = []
        for i in range(len(porcentajes)-1, -1, -1):
            porcentaje_1 = activo1*porcentajes[i]
            porcentaje_2 = activo2*(100-porcentajes[i])
            resultado.append(porcentaje_2+porcentaje_1)
        return pd.DataFrame(resultado)













