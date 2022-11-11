sueldo = 10
#pedir horas semanales trabajo
horasTrabajo = 0
diasSemana = ["lunes", "martes", "miercoles", "jueves", "viernes", "sabado"]
for dia in diasSemana:
    horasTrabajo += int(input(f"¿Cuantas horas trabajas el {dia}? "))

print(horasTrabajo*sueldo)