from random import shuffle

from domain.modelo.baraja import Baraja
from domain.modelo.carta import Carta


def crear_baraja():
    baraja = Baraja()
    for palo in Carta.PALOS:
        for numero in Carta.NUMEROS:
            baraja.cartas.append(Carta(numero, palo))
    return baraja

def mezclar_baraja(baraja):
    shuffle(baraja)
    


    