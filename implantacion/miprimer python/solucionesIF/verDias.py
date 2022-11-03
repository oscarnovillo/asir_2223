#pedir mes
mes = int(input("Introduce el mes: "))


#sacar dias que tiene el mes
dias = 0
hayError = False

if (mes == 1 or mes == 3 or mes == 5 or mes == 7 or mes == 8 or mes == 10 or mes == 12):
    dias = 31
elif (mes == 4 or mes == 6 or mes == 9 or mes == 11):
    dias = 30
elif (mes == 2):
    dias = 28
else:
    hayError = True


#salida del programa
if (not hayError):
    print("El mes", mes, "tiene", dias, "dias")
else:
    print("Error")

