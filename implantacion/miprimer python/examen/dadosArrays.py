from random import randint

TEXTO_TURNO = "Turno de %s"

nombresJugadores = ["", ""]
nombresJugadores[0] = input("Nombre del jugador 1: ")
nombresJugadores[1] = input("Nombre del jugador 2: ")

puntosJugador = [0,0]
puntosJugador1 = 0
puntosJugador2 = 0

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

while puntosJugador[0] < 3 and puntosJugador[1] < 3:
    dosDado = randint(2,12)
    print("El resultado de los dados es: ",dosDado)

    print("turno jugador "+nombresJugadores[turnoJugador])

    eleccionJugador = input("¿ que eliges par o  impar? ")
    ##turno jugador
    if eleccionJugador == "par" and (dosDado % 2) ==0:
        puntosJugador[turnoJugador] += 1
        print("Punto para",nombresJugadores[turnoJugador])
    elif eleccionJugador == "impar" and (dosDado % 2) ==1:
        puntosJugador[turnoJugador] += 1
        print("Punto para",nombresJugadores[turnoJugador])
    else:
        puntosJugador[(turnoJugador+1)%2] += 1
        print("Punto para",nombresJugadores[(turnoJugador+1)%2])

    #cambio turno
    turnoJugador = (turnoJugador + 1) % 2

if (puntosJugador[0] == 3):
    print("Ha ganado el jugador 1")
else:
    print("ganador el 2")

