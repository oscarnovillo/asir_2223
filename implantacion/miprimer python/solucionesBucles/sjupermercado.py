#pedir dia semana
dia = input("¿Que dia es hoy? ")

mensaje = "Hoy es domingo, no hay que trabajar"

if (dia != "domingo"):
    #quien eres
    nombre = input("¿Como te llamas? ")
    #pedir nombre producto
    nombreProducto = input("¿Que producto quieres comprar? ")
    #pedir cantidad producto
    cantidadProducto = int(input("¿Cuantos productos quieres comprar? "))
    #pedir nombre producto1
    nombreProducto1 = float(input("¿Cual es el precio del producto? "))
    #pedir cantidad producto2
    cantidadProducto2 = int(input("¿Cuantos productos quieres comprar? "))
    descuento = 1
    #calcular precio producto
    if (nombreProducto == "leche"):
        precioProducto = 1
    elif (nombreProducto == "pan"):
        precioProducto = 0.5

    if (dia == "lunes"):
        if (nombreProducto == "leche"):
            descuento = 0.8
    elif (dia == "martes"):
        descuento = 1.2
    elif (dia == "miercoles"):
        if (nombreProducto == "pan"):
            cantidadProducto = cantidadProducto // 2 + cantidadProducto % 2
    elif (dia == "viernes"):
        descuento = 0.3

    #ver cliente
    if (nombre == "carlos"):
        if (nombreProducto=="leche") or (nombreProducto=="pan"):
            descuento -= 0.1
    else (nombre == "mrMuro"):
        descuento = 1.5

    #calcular precio total
    precioTotal = (nombreProducto*cantidadProducto*descuento) 


print(mensaje)