from backend.Activo import *
from .CargarInformacion import CargarInformacion
from backend.Markowitz import *
from .Markowitz import Markowitz
import numpy as np


class CarteraDeInversiones:
    def __init__(self, nombre, periodo, archivo):
        self.nombre = nombre
        self.periodo = periodo
        self.archivo = archivo
        self.activos = {}
        self.cargar_informacion = CargarInformacion(self.archivo)
        self.modelo_markowitz = None

    def verificar_si_existe_activo(self, simbolo_activo):
        if simbolo_activo in self.activos.keys():
            return True
        else:
            return False

    def agregar_activo(self, nombre, simbolo):
        if not self.verificar_si_existe_activo(simbolo):
            activo = Activo(nombre, simbolo)
            activo.descargar_datos(self.periodo)
            self.activos[simbolo] = activo
            self.cargar_informacion.guardar_archivo(self)
        else:
            return

    def eliminar_activo(self, simbolo_activo):
        if self.verificar_si_existe_activo(simbolo_activo):
            del self.activos[simbolo_activo]
            self.cargar_informacion.guardar_archivo(self)
        else:
            return

    def cargar_cartera(self):
        cartera = self.cargar_informacion.cargar_archivo()
        if cartera is not None:
            self.nombre = cartera.nombre
            self.periodo = cartera.periodo
            self.activos = cartera.activos
            self.modelo_markowitz = Markowitz(self)
        else:
            return

    def rentabilidad_esperada(self):
        tabla = self.modelo_markowitz.calcular_rentabilidad_cartera_de_inversion()
        lista_activo1 = pd.DataFrame([i for i in range(0, 101, 20)])
        lista_activo2 = pd.DataFrame([i for i in range(100, -1, -20)])
        dp_concatenado = pd.concat([lista_activo1, lista_activo2, tabla], axis=1)
        return tabulate(dp_concatenado, headers=["Activo 1", "Activo 2", "Rendimiento esperado"])

    def riesgo_cartera(self):
        tabla = self.modelo_markowitz.calcular_riesgo_cartera_de_inversion()
        lista_activo1 = pd.DataFrame([i for i in range(0, 101, 20)])
        lista_activo2 = pd.DataFrame([i for i in range(100, -1, -20)])
        dp_concatenado = pd.concat([lista_activo1, lista_activo2, tabla], axis=1)
        return tabulate(dp_concatenado, headers=["Activo 1", "Activo 2", "Riesgo del portafolio"])
















