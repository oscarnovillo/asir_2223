# pedir numero
numero = int(input("numero de lineas "))


for i in range(1,numero+1):
    mensaje = ""
    for j in range(i):
        mensaje += "*"
    print(mensaje)


for i in range(numero,0,-1):
    mensaje = ""
    for j in range(i):
        mensaje += "*"
    print(mensaje)

#     *
#    **
#   ***
#  ****
# *****
for i in range(numero-1,0,-1):
    mensaje = ""
    for j in range(i):
        mensaje += " "
    for j in range(numero-i):
        mensaje += "*"
    
    print(mensaje)

#     *
#    * *
#   * * *
#  * * * *
# * * * * *
