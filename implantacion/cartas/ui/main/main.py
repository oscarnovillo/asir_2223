from domain.modelo.jugador import Jugador
from domain.modelo.baraja import Baraja
from domain.servicios.servicios_cartas import ServiciosCartas


# ejecucion cosas
def main():
    serviciosCartas = ServiciosCartas()
    baraja : Baraja = serviciosCartas.crear_baraja()

    serviciosCartas.mezclar_baraja(baraja.cartas)
    
    #Pedir 2 jugadores

    # Combat cartas


    # sacar una carta para cada jugador

    #un punto al jugador que la tenga mas grande

    # al final cuando se acaba la baraja se dice quien gana


    
    carta = baraja.siguiente_carta()
    while (carta != None):
        print(carta)
        carta = baraja.siguiente_carta()
    
        
    
    
    
    for carta in baraja.cartas:
        print(carta)

