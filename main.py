from backend.Cartera import *
from backend.Activo import *

if __name__ == '__main__':
    cartera = CarteraDeInversiones("Primera", "1mo", "cartera.txt")
    cartera.cargar_cartera()
    cartera.agregar_activo("Ecopetrol", "EC")







