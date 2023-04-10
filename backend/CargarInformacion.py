from .Activo import Activo


class CargarInformacion:
    def __init__(self, archivo):
        self.archivo = archivo

    def cargar_archivo(self):
        from backend.Cartera import CarteraDeInversiones
        cartera = CarteraDeInversiones("", "", self.archivo)
        with open(self.archivo, "r") as f:
            data = f.readlines()
            cartera.nombre = data[0].strip()
            cartera.periodo = data[1].strip()
            activos_dict = {}
            for i in range(2, len(data)):
                activo_data = data[i].strip().split(",")
                nombre = activo_data[0]
                simbolo = activo_data[1]
                activo = Activo(nombre, simbolo)
                activo.descargar_datos(cartera.periodo)
                activos_dict[simbolo] = activo
            cartera.activos = activos_dict
        return cartera

    def guardar_archivo(self, cartera):
        with open(self.archivo, "a") as f:
            f.write(cartera.nombre + "\n")
            f.write(cartera.periodo + "\n")
            for simbolo, activo in cartera.activos.items():
                if simbolo not in cartera.activos.keys():
                    f.write("{},{},{},{},{},{}\n".format(activo.nombre, simbolo, ",".join(str(precio) for precio in activo.open), ",".join(str(precio) for precio in activo.close), ",".join(str(precio) for precio in activo.high), ",".join(str(precio) for precio in activo.low)))
                else:
                    return