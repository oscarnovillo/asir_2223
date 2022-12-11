from random import randint

TEXTO_TURNO = "Turno de %s"

nombreJugador1 = input("Nombre del jugador 1: ")
nombreJugador2 = input("Nombre del jugador 2: ")
puntosJugador1= 0
puntosJugador2= 0
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

while puntosJugador1 < 3 and puntosJugador2 < 3:
    dosDado = randint(2,12)
    print("El resultado de los dados es: ",dosDado)

    if turnoJugador == 0:
        nombreJugadorConTurno = nombreJugador1
    else:
        nombreJugadorconTurno = nombreJugador2

    print(TEXTO_TURNO.format(nombreJugadorConTurno))


    eleccionJugador = input("¿ que eliges par o  impar? ")
    ##turno jugador
    if turnoJugador == 0:
        if eleccionJugador == "par" and (dosDado % 2) ==0:
            puntosJugador1 += 1
            print("Punto para",nombreJugador1)
        elif eleccionJugador == "impar" and (dosDado % 2) ==1:
            puntosJugador1 += 1
            print("Punto para",nombreJugador1)
        else:
            puntosJugador2 += 1
            print("Punto para",nombreJugador2)
    else:
        if eleccionJugador == "par" and (dosDado % 2) ==0:
            puntosJugador2 += 1
            print("Punto para",nombreJugador2)
        elif eleccionJugador == "impar" and (dosDado % 2) ==1:
            puntosJugador2 += 1
            print("Punto para",nombreJugador2)
        else:
            puntosJugador1 += 1
            print("Punto para",nombreJugador1)

    #cambio turno
    turnoJugador = (turnoJugador + 1) % 2




if (puntosJugador1 == 3):
    print("Ha ganado el jugador 1")
else:
    print("ganador el 2")

