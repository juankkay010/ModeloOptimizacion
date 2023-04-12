from typing import Optional
from .Usuario import *


class Sofwtare:
    def __init__(self):
        self.usuarios = {}

    def buscar_usuario(self, username) -> Optional[Usuario]:
        if username in self.usuarios.keys():
            return self.usuarios[username]
        else:
            return None

    def registrar_usuario(self, username, password):
        if self.buscar_usuario(username) is None:
            usuario = Usuario(username, password)
            self.usuarios[username] = usuario
        else:
            return




