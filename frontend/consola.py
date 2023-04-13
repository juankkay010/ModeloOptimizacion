import sys
from backend.Software import Software
from backend.Excepciones import *


class Consola:
    def __init__(self):
        self.software = Software()
        self.opciones = {
            "1": self.registrarse,
            "2": self.iniciar_sesion,
            "3": self.salir
        }
        self.menu_opciones_mostrar = {
            "1": self.crear_cartera,
            "2": self.agregar_activo,
            "3": self.eliminar_activo,
            "4": self.seleccionar_activo,
            "7": self.salir

        }

    def mostrar_menu(self):
        print("""
            \n
              BIENVENIDO A OPTIMICE SU CARTERA
            ====================================
            Menú de opciones:\n
            1. Registrarse
            2. Iniciar Sesión
            3. Salir
            ====================================
            """)

    def mostrar_segundo_menu(self):
        print("""
            \n
            ====================================
            Menú de opciones:\n
            1. Crear Cartera
            2. Agregar un activo a su cartera
            3. Eliminar un activo de su cartera
            4. Ver informacion sobre un activo
            5. Calcular la rentabilidad esperada de su cartera
            6. Calcular el riesgo de su cartera
            7. Salir
            ====================================
            """)

    def ejecutar(self):
        while True:
            self.mostrar_menu()
            opcion = input("Seleccione una opción: ")
            accion = self.opciones.get(opcion)
            if accion is not None:
                if accion() is False:
                    break
                elif accion == self.iniciar_sesion:
                    self.ejecutar_segundo_menu()
                    return False
            else:
                print(f"\n {opcion} no es una opción válida")

    def ejecutar_segundo_menu(self):
        while True:
            self.mostrar_segundo_menu()
            opcion = input("Seleccione una opción: ")
            accion = self.menu_opciones_mostrar.get(opcion)
            if accion is not None:
                accion()
            else:
                print(f"\n {opcion} no es una opción válida")

    def registrarse(self):
        print("\n>>> REGISTRARSE")
        username = input("Ingrese un nombre de usuario: ")
        password = input("Ingrese una contraseña: ")
        try:
            self.software.registrar_usuario(username, password)
            print("INFO: El usuario se registró exitosamente")
        except UsuarioExistente as err:
            print(err.mensaje)

    def iniciar_sesion(self):
        print("\n>>> INICIAR SESIÓN")
        username = input("Ingrese un nombre de usuario: ")
        password = input("Ingrese una contraseña: ")
        try:
            self.software.iniciar_sesion(username, password)
            print("Ingreso exitoso")
            self.mostrar_segundo_menu()
            return True
        except EspaciosSinRellenar as err:
            print(err.mensaje)
        except CuentaNoExistenteError as err:
            print(err.mensaje)
        except ContrasenaInvalida as err:
            print(err.mensaje)

    def salir(self):
        sys.exit(0)

    def crear_cartera(self):
        nombre = input("Ingrese el nombre de la cartera: ")
        periodo = input("Ingrese el periodo en el cual se encontrara su cartera: ")
        archivo = input("Ingrese la ruta donde se guardara la información: ")
        try:
            usuario_actual = self.software.get_usuario_actual()
            if usuario_actual is not None:
                usuario_actual.crear_cartera(nombre, periodo, archivo)
                print("INFO: Cartera creada exitosamente")
        except CarteraExistente as err:
            print(err.mensaje)

    def agregar_activo(self):
        nombre = input("Ingrese el nombre del activo: ")
        simbolo = input("Ingrese el simobolo del activo: ")
        try:
            usuario_actual = self.software.get_usuario_actual()
            if usuario_actual is not None:
                usuario_actual.cartera.agregar_activo(nombre, simbolo)
                print(f"El activo {simbolo} se ha agregado correctamente")
        except ActivoExistente as err:
            print(err.mensaje)

    def eliminar_activo(self):  # No se ha implementado
        pass

    def seleccionar_activo(self):
        usuario_actual = self.software.get_usuario_actual()
        if usuario_actual is not None:
            activos = usuario_actual.cartera.get_activos()
            if activos:
                print("==== LISTA DE ACTIVOS ====")
                for i, activo in enumerate(activos, 1):
                    print(f"{i}: {activo.simbolo}")
                opcion = input("Seleccione el número del activo que desea ver: ")
                try:
                    opcion = int(opcion)
                    if 0 < opcion <= len(activos):
                        activo_seleccionado = activos[opcion - 1]
                        print(activo_seleccionado.tabla_informacion_activo())
                    else:
                        print(f"{opcion} no es una opción válida")
                except ValueError:
                    print("Opción inválida")
            else:
                print("La cartera no tiene activos")








