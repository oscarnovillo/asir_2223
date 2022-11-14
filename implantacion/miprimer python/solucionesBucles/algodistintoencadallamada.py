variable = True
numero = 0
mensaje = ""

for i in range(10):
    mensaje = ""
    for j in range(i):
        if variable:
            mensaje += "Hola "
        else:
            mensaje +="Adios "

    print(mensaje)    

    variable = not variable

    