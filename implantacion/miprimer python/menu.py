from nis import match


def ejercicio3():
    #pedir nombre
    nombre = input("ingrese su nombre: ")


    #poner primeraa letra en mayusculas

    if (len(nombre) > 2):
        nombre = nombre[0].lower() + nombre[1].upper()+ nombre[2:].lower()


    #mostrar nombre
    print(nombre)

#mostrar menu opciones
print("1. calcular raiz cuadrada")
print("2. calcular raiz cubica")
print("3. calcular distancia entre dos puntos")
print("4. calcular total de monedas")
print("5. calcular distancia entre dos numeros")
print("6. calcular distancia entre dos numeros")


#pedir opcion de menu
opcion = int(input("ingrese una opcion: "))

#ejecutar opcion
if opcion == 1:
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
elif opcion == 2:
    #pedir respuestas correctas, incorrectas y en blanco
    correctas = int(input("ingrese respuestas correctas: "))
    incorrectas = int(input("ingrese respuestas incorrectas: "))
    enBlanco = int(input("ingrese respuestas en blanco: "))

    #calcular puntaje
    puntaje = correctas * 5 - incorrectas * 1 

    #mostrar puntaje
    print("el puntaje es: ", puntaje)

    numeroPreguntas = correctas + incorrectas + enBlanco

    valorMaximoTest = numeroPreguntas * 5

    notaFinalSobre10 = puntaje / valorMaximoTest * 10

    #mostrar puntaje sobre 10
    print("el puntaje sobre 10 es: {:.2f}".format(notaFinalSobre10))

elif opcion == 3:
    ejercicio3()


