#pedir numero
numero = int(input("ingrese un numero: "))


#ver si es par
if numero % 2 == 0:
    print("es par")
else:
    print("es impar")

#ver si es mayor o igual a 100
if numero >= 200:
    print("es mayor o igual a 200")
elif numero >= 150:
        print("es menor a 200 mayor 150")
elif numero >= 100:
    print("es menor a 150 mayor 100")



if numero %3 == 0:
    if numero > 30 :
        print("es multiplo de 3 y mayor a 30")
    else:
        print("es multiplo de 3 y menor a 30")
elif numero % 5 == 0:
    print("es multiplo de 5")


if (numero % 3 == 0 and numero > 30) or (numero % 5 == 0 and numero <=10):
    print("es multiplo de 3 y mayor a 30 o es multiplo de 5 y menor a 10")




