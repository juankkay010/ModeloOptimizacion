class ErrorSoftware(Exception):
    def __init__(self, mensaje):
        self.mensaje = mensaje


class UsuarioExistente(ErrorSoftware):
    def __init__(self, mensaje):
        super().__init__(mensaje)


class CuentaNoExistenteError(ErrorSoftware):
    def __init__(self, mensaje):
        super().__init__(mensaje)


class ContrasenaInvalida(ErrorSoftware):
    def __init__(self, mensaje):
        super().__init__(mensaje)


class EspaciosSinRellenar(ErrorSoftware):
    def __init__(self, mensaje):
        super().__init__(mensaje)


class CarteraExistente(ErrorSoftware):
    def __init__(self, mensaje):
        super().__init__(mensaje)