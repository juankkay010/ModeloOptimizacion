from backend.Cartera import *

if __name__ == '__main__':
    cartera = CarteraDeInversiones("Primera", "1y", "cartera.txt")
    cartera.cargar_cartera()
    print(cartera.rentabilidad_esperada())





