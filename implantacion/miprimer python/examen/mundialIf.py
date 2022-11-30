golesMessi = int(input("Cuantos goles ha marcado Messi? "))
paradasUnai = int(input("Cual es el porcentaje de paradas de Unai? "))
posesionEspaña = int(input("Posesion media de España: "))
tarjetasRojasBrasil = int(input("Tarjetas rojas a Brasil: "))
golesMbape = int(input("Goles de mbape: "))
primasArabia = int(input("Primas de Arabia: "))

if (golesMessi>8):
    print("Gana Argentina")
elif (golesMessi>4 and golesMessi<8) :
    if (paradasUnai>90 and tarjetasRojasBrasil>1):
        print("Gana Alemania")
    elif (posesionEspaña>75 and golesMbape<3):
        print("Gana España")
    elif (tarjetasRojasBrasil==0 and golesMbape>5):
        print("Gana Francia")
    elif (golesMbape>5 or posesionEspaña<60):
        print("Gana Brasil") 
elif (primasArabia>=10000000):
    print("Gana Arabia")
elif (primasArabia<10000000 and tarjetasRojasBrasil>3 and golesMbape<3 and posesionEspaña<50 and paradasUnai<50):
    print("Gana Japón")
else:
    print("No se sabe quien ha ganado.")
