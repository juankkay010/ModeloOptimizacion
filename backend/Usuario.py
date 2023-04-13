from typing import Optional
from .Cartera import *
from .Excepciones import *


class Usuario:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.cartera = CarteraDeInversiones("", "", "")

    def buscar_cartera(self, nombre) -> Optional[CarteraDeInversiones]:
        if nombre == self.cartera.nombre:
            return self.cartera
        return None

    def crear_cartera(self, nombre, periodo, archivo):
        if self.buscar_cartera(nombre) is None:
            self.cartera = CarteraDeInversiones(nombre, periodo, archivo)
        else:
            raise CarteraExistente("La cartera ya existe con ese nombre")





