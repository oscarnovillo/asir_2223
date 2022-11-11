#menu

opcion = 0

while opcion!=5: 
    print("1. Sumar")
    print("2. Restar")
    print("3. Multiplicar")
    print("4. Dividir")
    print("5. Salir")

    opcion = 0
      # condicion HASTA opcion >=1 and opcion <=5
    while opcion < 1 or opcion > 5:
        opcionString =input("¿Que opcion desea? ") 
        if (opcionString.isdigit()):
            opcion = int(opcionString)
        else:
            print("Error, no es un numero")



    if (opcion == 1):
        print("Sumar")
    elif (opcion == 2):
        print("Restar")
    elif (opcion == 3):
        print("Multiplicar")
    elif (opcion == 4):
        print("Dividir")
    elif (opcion == 5):
        print("Salir")
    else:
        print("Opcion no valida")