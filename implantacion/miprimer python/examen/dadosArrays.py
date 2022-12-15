from random import randint
from clases.Jugador import Jugador



TEXTO_TURNO = "Turno de %s"


nombreJugador = input("Nombre del jugador 1: ")
apellidoJugador = input("Apellido del jugador 1: ")
jugador1 = Jugador(nombreJugador,apellidoJugador)
jugador1.nombreCompleto
nombreJugador = input("Nombre del jugador 2: ")
jugador2 = Jugador(nombreJugador,"gomez")

jugadores = [jugador1,jugador2]


print(jugadores[0])


turnoJugador = 0

eleccionJugador1 = int(input("¿1 Cara o 0 Cruz? "))
moneda = randint(0,1)
print("La moneda ha salido: ",moneda)
if eleccionJugador1 == moneda:
    print("Empieza Jugador 1")
    turnoJugador = 0
else:
    print("Empieza Jugador 2")
    turnoJugador = 1

while jugadores[0].puntos < 3 and jugadores[1].puntos < 3:
    dosDado = randint(2,12)
    print("El resultado de los dados es: ",dosDado)

    print("turno jugador "+str(jugadores[turnoJugador]))

    eleccionJugador = input("¿ que eliges par o  impar? ")
    ##turno jugador
    if eleccionJugador == "par" and (dosDado % 2) ==0:
        jugadores[turnoJugador].puntos += 1
        print("Punto para",jugadores[turnoJugador].nombre)
    elif eleccionJugador == "impar" and (dosDado % 2) ==1:
        jugadores[turnoJugador].puntos += 1
        print("Punto para",jugadores[turnoJugador].nombre)
    else:
        jugadores[(turnoJugador+1)%2].puntos += 1
        print("Punto para",jugadores[(turnoJugador+1)%2].puntos)

    #cambio turno
    turnoJugador = (turnoJugador + 1) % 2

if (jugadores[0].puntos == 3):
    print("Ha ganado el jugador 1")
else:
    print("ganador el 2")

