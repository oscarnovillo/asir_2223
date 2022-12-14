from enum import Enum

class Carta:
    class PALOS(Enum):
        OROS = 0
        ESPADAS = 1
        COPAS = 2
        BASTOS = 3
        
    class NUMEROS(Enum):
        AS = 1
        DOS = 2
        TRES = 3
        CUATRO = 4
        CINCO = 5
        SEIS = 6
        SIETE = 7
        OCHO = 8
        NUEVE = 9
        DIEZ = 10
        JOTA = 11
        DAMA = 12
        REY = 13   

    def __init__(self, valor : NUMEROS, palo:PALOS):
        self.valor = valor
        self.palo = palo
        
    def __str__(self) :
        return "Cartita: " + str(self.valor.name) + " de " + str(self.palo.name)


