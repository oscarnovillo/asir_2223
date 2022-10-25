horas = 23
minutos = 59
segundos = 59

print("la hora a la que sale  es ",str(horas)+":"+str(minutos).format("%2s")+":"+str(segundos))


print("la cantidad de segundos es: ",(horas*3600)+(minutos*60)+segundos)

tiempo = int(input("ingrese la cantidad de segundos: "))

horas = horas + tiempo // 3600

minutos = minutos + (tiempo % 3600) // 60
horas += minutos // 60
minutos = minutos % 60
horas = horas % 24

segundos = segundos + (tiempo % 3600) % 60
minutos += segundos // 60
segundos = segundos % 60




print("la hora a la que llega  es ",str(horas)+":"+str(minutos)+":"+str(segundos))



segundos += tiempo
minutos += segundos // 60
segundos = segundos % 60
horas += minutos // 60
minutos = minutos % 60
horas = horas % 24


print("la hora a la que llega  es ",str(horas)+":"+str(minutos)+":"+str(segundos))



