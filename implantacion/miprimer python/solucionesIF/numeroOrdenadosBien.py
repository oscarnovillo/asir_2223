#pedir 3 numeros
numero1 = int(input("ingrese un numero: "))
numero2 = int(input("ingrese un numero: "))
numero3 = int(input("ingrese un numero: "))

lista  = {numero1, numero2, numero3}
listaOrdenada = sorted(lista)
print(listaOrdenada.reverse())

mayor = 0
menor = 0
medio = 0

#buscar el mayor
print ("el mayor es ")
if numero1 >= numero2 and numero1 >= numero3:
    mayor=numero1
    if (numero2 >= numero3):
        medio=numero2
        menor=numero3
    else:
        medio=numero3
        menor=numero2
elif numero2 >= numero1 and numero2 >= numero3:
    mayor = numero2
    if (numero1 >= numero3):
        medio=numero1
        menor=numero3
    else:
        medio=numero3
        menor=numero1
elif numero3 >= numero1 and numero3 >= numero2:
    mayor = numero3
    if (numero1 >= numero2):
        medio=numero1
        menor=numero2
    else:
        medio=numero2
        menor=numero1



print("el mayor es: ", mayor)
print("el medio es: ", medio)
print("el menor es: ", menor)