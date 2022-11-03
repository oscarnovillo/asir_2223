#pedir minutos de la llamada, dia de la semana, turno
minutosLlamada = int(input("¿Cuantos minutos ha durado la llamada? "))
diaSemana = input("¿Que dia de la semana es? (L, M, X, J, V, S, D) ")
turno = input("¿En que turno ha sido? (M, T) ")

#precio de la llamada
precioLlamada = 1

if (minutosLlamada >= 6 ):
    precioLlamada += 0.80

if (minutosLlamada >= 8):
    precioLlamada += 0.70

if (minutosLlamada > 10 ):
    precioLlamada += 0.50




#descuento por dia si es Domingo
porcentajeExtra = 0.03

if (diaSemana != "D"):
    if (turno == "M"):
        porcentajeExtra = 0.15
    elif (turno == "T"):
        porcentajeExtra = 0.10

precioLlamada = precioLlamada * (1+porcentajeExtra)

print("El precio de la llamada es de", precioLlamada, "euros")
