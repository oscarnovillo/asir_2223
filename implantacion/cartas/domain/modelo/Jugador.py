class Jugador:

    def __init__(self, nombre :str,apellidos:str ,puntos:int =0):
        self.nombre = nombre
        self.apellidos = apellidos
        self.puntos = puntos

    def nombre_completo(self):  
        return self.nombre + " " + self.apellidos

    def __str__(self):
        return self.nombre + " " + self.apellidos + " " + str(self.puntos)
