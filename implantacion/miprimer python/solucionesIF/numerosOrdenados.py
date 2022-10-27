#pedir 3 numeros
numero1 = int(input("ingrese un numero: "))
numero2 = int(input("ingrese un numero: "))
numero3 = int(input("ingrese un numero: "))

#buscar el mayor
print ("el mayor es ")
if numero1 >= numero2 and numero1 >= numero3:
    print(numero1)
elif numero2 >= numero1 and numero2 >= numero3:
    print(numero2)
elif numero3 >= numero1 and numero3 >= numero2:
    print(numero3)

# mirar el del medio
if (numero1 <= numero2 and numero1 >= numero3) or (numero1 >= numero2 and numero1 <= numero3):
    print(numero1)
elif numero2 <= numero1 and numero2 >= numero3 or numero2 >= numero1 and numero2 <= numero3:
    print(numero2)
elif numero3 <= numero1 and numero3 >= numero2 or numero3 >= numero1 and numero3 <= numero2:
    print(numero3)    


# mirar el menor
if numero1 <= numero2 and numero1 <= numero3:
    print(numero1)
elif numero2 <= numero1 and numero2 <= numero3:
    print(numero2)
elif numero3 <= numero1 and numero3 <= numero2:
    print(numero3)    

