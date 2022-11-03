#pedir dia, mes,año
dia = int(input("Introduce el dia: "))
mes = int(input("Introduce el mes: "))
año = int(input("Introduce el año: "))

isBisiesto = (año % 4 == 0 and año % 100 != 0 or año % 400 == 0)
isMesCon31 = (mes == 1 or mes == 3 or mes == 5 or mes == 7 or mes == 8 or mes == 10 or mes == 12)



if (isMesCon31 and (dia >= 1 and dia <= 31)):
    print("La fecha es correcta")
elif (mes == 4 or mes == 6 or mes == 9 or mes == 11):
    if (dia >= 1 and dia <= 30):
        print("La fecha es correcta")
elif (mes == 2):
    if (dia >= 1 and dia <= 28):
        print("La fecha es correcta")
    elif (dia == 29 and isBisiesto):
        print("La fecha es correcta")
else:
    print("La fecha no es correcta")



