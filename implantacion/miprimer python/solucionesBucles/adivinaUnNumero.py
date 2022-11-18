#un usuario al entrar dice el dinero que tiene
#Apuesta una cantidad de ese dinero en cada partida y tiene diez oportunidades para adivinar un numero aleatorio, 
#No puede apostar mas del dinero que le queda
#con mensaje diciendo si es mayor o no
#si lo advina gana lo apostado si falla pierde lo apostado
#con la posiblidad de volver a jugar otra vez si le queda dinero
from random import randint

print("Bienvenido al juego de adivinar el numero misterioso.")
dineroDisponible=int(input("Cuanto dinero tiene? "))


volverAJugar = "si"

while volverAJugar == "si":
    #Declaramos el fin del programa en caso de que no quiera jugar.
    dineroApostado=int(input("¿Cuanto dinero quiere apostar? "))
    while dineroApostado>dineroDisponible:
        dineroApostado=int(input("Ingrese una cantidad valida. "))
    
    numeroAleatorio=randint(1,100)
    print("Dispone de un máximo de 10 intentos.")
    vecesIntentado=0
    numeroIntentoUsuario = -1
    while numeroIntentoUsuario!=numeroAleatorio and vecesIntentado<10:
        numeroIntentoUsuario=int(input("Adivine el numero entre 0 y 100.\n"))
        vecesIntentado+=1
        if numeroIntentoUsuario>numeroAleatorio:
            print("El numero es menor. (Intento "+str(vecesIntentado)+")")
        elif numeroIntentoUsuario<numeroAleatorio:
            print("El numero es mayor. (Intento "+str(vecesIntentado)+")")
            
    if numeroIntentoUsuario==numeroAleatorio:
        dineroDisponible+=dineroApostado
        print("CORRECTO!. Recoja sus ganancias.")
    else:
        print(" se te acabaron los intentos. Pierde su apuesta.")
        dineroDisponible-=dineroApostado
    print("Dispone de "+str(dineroDisponible)+"€")
    volverAJugar=input("¿Quiere volver a apostar? ")
    #de aqui vuelve al principio del while

print("al final de las partidas te vas con "+str(dineroDisponible)+"€")