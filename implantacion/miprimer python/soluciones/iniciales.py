#pedir nombre
nombre = input("ingrese su nombre: ")


#poner primeraa letra en mayusculas

if (len(nombre) > 2):
    nombre = nombre[0].lower() + nombre[1].upper()+ nombre[2:].lower()


#mostrar nombre
print(nombre)