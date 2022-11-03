#pedir cuanto alumnos
numeroAlumnosExcursion = int(input("¿Cuantos alumnos son? "))

#lo que hay que calcular
precioAutobus = 0
precioPorAlumno = 0

if numeroAlumnosExcursion >= 100:
    precioPorAlumno = 65
elif (numeroAlumnosExcursion >= 50 
    or numeroAlumnosExcursion <= 99):
    precioPorAlumno = 70
elif (numeroAlumnosExcursion >= 30
     or numeroAlumnosExcursion <= 49):
     precioPorAlumno = 95    
elif numeroAlumnosExcursion < 30:
     precioAutobus = 4000
     precioPorAlumno = precioAutobus / numeroAlumnosExcursion

if (numeroAlumnosExcursion >= 30):
    precioAutobus = precioPorAlumno * numeroAlumnosExcursion

print("El precio del autobus es de", precioAutobus, "euros")
print("El precio por alumno es de", precioPorAlumno, "euros")