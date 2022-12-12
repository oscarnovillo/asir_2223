class Jugador:

    def __init__(self, nombre,apellidos,puntos=0):
        self.nombre = nombre
        self.apellidos = apellidos
        self.puntos = puntos

    def nombreCompleto(self):  
        return self.nombre + " " + self.apellidos

    def __str__(self):
        return self.nombre + " " + self.apellidos + " " + str(self.puntos)
