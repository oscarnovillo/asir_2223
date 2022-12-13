import sys

from domain.modelo.baraja import Baraja
from domain.servicios.servicios_cartas import crear_baraja, mezclar_baraja


# ejecucion cosas
def main():
    print(__name__)
    baraja : Baraja = crear_baraja()
    # mezclar_baraja(baraja.cartas)
    
    #Pedir jugadores
    
    carta = baraja.siguiente_carta()
    while (carta != None):
        print(carta)
        carta = baraja.siguiente_carta()
    
    
    
    # for carta in baraja.cartas:
    #     print(carta)