#pedir nota, edad, sexo
nota = int(input("ingrese la nota: "))
edad = int(input("ingrese la edad: "))
sexo = input("ingrese el sexo: ")



if (nota >=5 and edad >=18):
    if sexo.lower() == "f":
        print("aprobada")
    elif sexo.lower() == "m":
        print("posible")
    else:
        print("error")
else:
    print("no aceptada")




