producto1 = "datil"
producto2 = "manzana"
producto3 = "pera"
producto4 = "uva"
producto5 = "sandia"
producto6 = "melon"
producto7 = "piña"
producto8 = "naranja"
producto9 = "mandarina"
producto10 = "platano"


# Crear una lista
productos = [producto1, producto2, producto3, producto4, producto5, producto6, producto7, producto8, producto9, producto10]
productos = ["melon", "piña", "naranja", "mandarina", "platano"]

personas = ["Juan", 3, "kk", 91888, ["Jose", "Ana"], "Luis", "Miguel", "Rosa", "Sofia"]
personas[0] = "Nuevo"

tupla = (1,2,3,4,5,6,7,8,9,10)
tupla[0] = 100

listaTupla = list(tupla)
noModificable = tuple(productos)
personasNoRepetidas = set(personas)

noseQueSaldra = dict(personas)

set = {1,2,3,4,5,1,1,1,6,7,8,9,10}



# Diccionario
personasFrutas = {"juan" : "melon","pedro": "piña"}
print(personasFrutas["juan"])