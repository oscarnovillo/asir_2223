alumnos = ["Juan0", "Ana1", "Pedro2", "Luis3", "Maria4"]

print(len(alumnos))

print(alumnos[len(alumnos)-1])

indice = 0
while indice < len(alumnos):
    print(alumnos[indice])
    indice += 1

for alumno in alumnos:
    print(alumno)

for i in range(0,10):
    print(i+1)


#ver un elemento
print(alumnos[0])
print(alumnos[-1])
print(alumnos[-5])

#Coger un subconjunto

print("subconjunto")
subListaAlumnos = alumnos[0:2]
for alumno in subListaAlumnos:
    print(alumno)


subListaAlumnos = alumnos[:-2]
for alumno in subListaAlumnos:
    print(alumno)

subListaAlumnos = alumnos[0:5:2]
for alumno in subListaAlumnos:
    print(alumno)


subListaAlumnos = alumnos[::-1]
for alumno in subListaAlumnos:
    print(alumno)

nombre = "juanito"
listaCaracteres = ["j","u","a","n","i","t","o"]
print(nombre[::-1])
print(nombre[2])






