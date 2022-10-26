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