from typing import Optional
import os
from .Usuario import *
from .Excepciones import *


class Software:
    def __init__(self):
        self.usuarios = {}
        self.usuario_actual = None
        self.cargar_datos_usuario()

    def get_usuario_actual(self):
        return self.usuario_actual

    def buscar_usuario(self, username) -> Optional[Usuario]:
        if username in self.usuarios.keys():
            return self.usuarios[username]
        else:
            return None

    def registrar_usuario(self, username, password):
        if self.buscar_usuario(username) is None:
            usuario = Usuario(username, password)
            self.usuarios[username] = usuario
            self.guardar_datos_usuario(usuario)
            return True
        else:
            raise UsuarioExistente("Este usuario ya se encuentra registrado")

    def iniciar_sesion(self, username, password):
        if username == "" or password == "":
            raise EspaciosSinRellenar("Debe rellenar todos los campos")
        if username in self.usuarios.keys():
            usuario = self.usuarios[username]
        else:
            raise CuentaNoExistenteError("Este usuario no se encuentra registrado")
        if usuario.password == password:
            self.usuario_actual = usuario
            return True
        else:
            raise ContrasenaInvalida("La contraseña es incorrecta")

    def cargar_datos_usuario(self):
        with open("Usuarios/usuarios.txt", "r") as f:
            line = f.readline()
            if line.strip() and ',' in line:
                data = line.split(",")
                usuarios = map(lambda data: Usuario(data[0], data[1]), [data])
                for usuario in usuarios:
                    self.usuarios[usuario.username] = usuario
            else:
                self.usuarios = {}

    def guardar_datos_usuario(self, usuario: Usuario):
        with open("Usuarios/usuarios.txt", "a") as f:
            f.write(f"{usuario.username},{usuario.password},{usuario.cartera.archivo}{os.linesep}")















