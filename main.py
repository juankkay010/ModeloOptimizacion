from backend.Cartera import *

if __name__ == '__main__':
    cartera = CarteraDeInversiones("Primera", "1mo", "cartera.txt")
    cartera.cargar_cartera()
    print(cartera.activos["CIB"].tabla_informacion_activo())







