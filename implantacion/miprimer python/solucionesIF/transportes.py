#pedir zona geografica, peso paquete
zonaGeografica = input("¿Que zona geografica es?: (1,2,3,4,5) ")
pesoPaquete = int(input("¿Cual es el peso del paquete? "))


#sacar precio del envio
precioEnvio = 0
precioPorKilo = 0
hayError = False

if (pesoPaquete > 5):
    hayError = True
else:
    if (zonaGeografica == "1"):
        precioPorKilo = 24
    elif (zonaGeografica == "2"):
        precioPorKilo = 20
    elif (zonaGeografica == "3"):
        precioPorKilo = 21
    elif (zonaGeografica == "4"):
        precioPorKilo = 10
    elif (zonaGeografica == "5"):
        precioPorKilo = 18

if(not hayError):
    precioEnvio = precioPorKilo * pesoPaquete


#salida del programa
if (not hayError):
    print("El precio del envio es", precioEnvio)
else:
    print("Error")
