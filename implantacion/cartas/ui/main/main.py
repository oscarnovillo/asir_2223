from operator import attrgetter

from domain.modelo.baraja import Baraja
from domain.modelo.jugador import Jugador
from domain.servicios.servicios_cartas import ServiciosCartas


# ejecucion cosas
def main():
    servicios_cartas: ServiciosCartas = ServiciosCartas()
    baraja: Baraja = servicios_cartas.crear_baraja()

    servicios_cartas.mezclar_baraja(baraja)

    # Pedir 2 jugadores

    # Combat cartas

    nombre = input("Introduce tu nombre: ")

    jugador: Jugador = Jugador(nombre, "apellidos")

    nombre = input("Introduce tu nombre: ")
    jugador2 = Jugador(nombre, "apellidos")
    jugador.nombre
    print(jugador.nombre_completo())

    # sacar dos carta, una para cada jugador

    # un punto al jugador que la tenga mas grande

    # al final cuando se acaba la baraja se dice quien gana

    carta = baraja.siguiente_carta()
    carta1 = baraja.siguiente_carta()
    while (carta != None):
        print(carta, carta1)
        carta = baraja.siguiente_carta()
        carta1 = baraja.siguiente_carta()

    # for i in range (0,40,2):
    #     miputamadre = baraja.cartas[i]
    #     tuputamadre = baraja.cartas[i+1]
    #     print("primera pareja de cartas",miputamadre,tuputamadre)

    print(max(baraja.cartas, key=attrgetter('valor.value')))

    print(sorted(baraja.cartas, key=attrgetter('valor.value', 'palo.value')))

    # for carta in baraja.cartas:
    #     print(carta)
