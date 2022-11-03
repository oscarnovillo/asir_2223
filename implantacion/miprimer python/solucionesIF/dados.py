#pedir valor de dado
valorDado = int(input("¿Que valor ha salido en el dado? "))


#sacar cara opuesta
caraOpuesta = ""
hayError = False

if (valorDado == 1):
    caraOpuesta = "seis"
elif (valorDado == 2):
    caraOpuesta = "cinco"
elif (valorDado == 3):
    caraOpuesta = "cuatro"
elif (valorDado == 4):
    caraOpuesta = "tres"
elif (valorDado == 5):
    caraOpuesta = "dos"
elif (valorDado == 6):
    caraOpuesta = "uno"
else:
    hayError = True


#salida del programa
if (not hayError):
    print("La cara opuesta es", caraOpuesta)
else:
    print("Error")

