from domain.modelo.carta import Carta


class Baraja:
    
    indice : int = 0
    def __init__ (self):
        self.cartas : list[Carta] = list()
        
    def siguiente_carta(self):
        if self.indice >= self.cartas.__len__():
            return None
        carta = self.cartas[self.indice]
        self.indice += 1
        return carta
    
    def dar_vuelta_baraja(self):
        self.indice = 0
