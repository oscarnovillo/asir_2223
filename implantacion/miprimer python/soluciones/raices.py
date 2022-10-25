import math

#pedir numero
numero = int(input("ingrese un numero: "))

#calcular raiz cuadrada
raiz = numero ** 0.5
raiz = math.sqrt(numero)


#calcular raiz cubica
raizCubica = numero ** (1/3)
raizCubica = pow(numero,1/3)



#mostrar datos
print("la raiz cuadrada es: ", raiz)
print("la raiz cubica es: ", raizCubica)