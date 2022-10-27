#pedir base y exponente
base = int(input("ingrese la base: "))
exponente = int(input("ingrese el exponente: "))

#calcular la potencia

potencia = 0

if base==1:
    potencia=1
elif base > 0 :
    if (exponente == 0):
        potencia = 1
    elif (exponente >0):
        potencia = base ** exponente
    elif (exponente <0):
        potencia = 1 / (base ** exponente)    
elif base <=0:
    print ("error")

if base==1:
    potencia=1
elif base > 0 and exponente == 0:
    potencia = 1
elif base > 0 and exponente >0:
        potencia = base ** exponente
elif base > 0 and exponente <0:
        potencia = 1 / (base ** exponente)    
elif base <=0:
    print ("error")



#imprimir el resultado
print("el resultado es: ", potencia)