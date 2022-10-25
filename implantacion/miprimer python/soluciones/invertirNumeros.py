#pedir numero
numero = int(input("ingrese un numero: "))

#sacar primer digito
primerDigito = numero // 10

#sacar segundo digito
segundoDigito = numero % 10


#mostrar numero invertido
print(str(segundoDigito)+str(primerDigito))