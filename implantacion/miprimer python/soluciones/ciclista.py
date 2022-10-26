#pedir horas minutos segundos
horas = int(input("ingrese las horas: "))
minutos = int(input("ingrese los minutos: "))
segundos = int(input("ingrese los segundos: "))
tiempo = int(input("tiempo tardado en segundos: "))


#calcular hora nueva
horaNueva = horas + tiempo // 3600
tiempo = tiempo % 3600
horaNueva = horaNueva % 24

minutoNuevo = minutos + tiempo // 60
segundoNuevo = segundos + tiempo % 60


#mostrar datos
print("la hora nueva es: {:0>2d}:{:0>2d}:{:0>2d} ".format(horaNueva, minutoNuevo, segundoNuevo))



