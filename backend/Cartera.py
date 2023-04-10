from backend.Activo import *
from .CargarInformacion import CargarInformacion


class CarteraDeInversiones:
    def __init__(self, nombre, periodo, archivo):
        self.nombre = nombre
        self.periodo = periodo
        self.archivo = archivo
        self.activos = {}
        self.cargar_informacion = CargarInformacion(self.archivo)

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
        self.nombre = cartera.nombre
        self.periodo = cartera.periodo
        self.activos = cartera.activos











