#pedir dia semana
dia = input("¿Que dia es hoy? ")
precioTotal = 0
mensaje = "Hoy es domingo, no hay que trabajar"
descuentoMartes = 0.2

if (dia != "domingo"):
    #quien eres
    nombre = input("¿Como te llamas? ")
    for i in range(5):
        #pedir nombre producto
        nombreProducto = input("¿Que producto quieres comprar? ")
        #pedir cantidad producto
        cantidadProducto = int(input("¿que cantidad de "+str(nombreProducto)+" quieres comprar? "))
        #pedir nombre producto1
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
            descuento = 1+descuentoMartes
        elif (dia == "miercoles"):
            if (nombreProducto == "pan"):
                cantidadProducto = cantidadProducto // 2 + cantidadProducto % 2
        elif (dia == "viernes"):
            descuento = 0.3

        #ver cliente
        if (nombre == "carlos"):
            if (nombreProducto=="leche") or (nombreProducto=="pan"):
                descuento -= 0.1
        elif (nombre == "mrMuro"):
            descuento = 1.5
            if (dia=="martes"):
                descuento += descuentoMartes

        #calcular precio total
        precioProducto = (cantidadProducto*descuento) 
        precioTotal += precioProducto
        print("El precio de este producto es {:.02f}".format(precioProducto))
        print(f"el dinero gastado que llevas es {precioTotal:.2f}")

    print(f"el precio total es {precioTotal:.2f}")
else:
    print(mensaje)