import sys

from domain.servicios.serviciosCartas import crear_baraja, mezclar_baraja


# ejecucion cosas
def main():
    print(sys.path)
    baraja = crear_baraja()
    mezclar_baraja(baraja.cartas)
    for carta in baraja.cartas:
        print(carta)