import math

# pedir los dos puntos x1,y1 y x2,y2
x1 = int(input("ingrese el primer numero: "))
y1 = int(input("ingrese el segundo numero: "))
x2 = int(input("ingrese el primer numero: "))
y2 = int(input("ingrese el segundo numero: "))


# calcular la distancia

#cuadrado de cada cateto
cateto1 = pow((x2 - x1),2)
cateto2 = (y2 - y1)**2


#raiz cuadrada de la suma de los catetos
distancia = math.sqrt(cateto1 + cateto2)


#mostrar datos
print("la distancia es: ", distancia)