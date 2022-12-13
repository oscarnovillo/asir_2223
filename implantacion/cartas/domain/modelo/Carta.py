from enum import Enum


class Carta:
    class PALOS(Enum):
        OROS = 1
        ESPADAS = 2
        COPAS = 3
        BASTOS = 4
        TUPUTA = 5
        
    class NUMEROS(Enum):
        AS = 1
        DOS = 2
        TRES = 3
        CUATRO = 4
        CINCO = 5
        SEIS = 6
        SIETE = 7
        SOTA = 10
        CABALLO = 11
        REY = 12    

    def __init__(self, valor : NUMEROS, palo:PALOS):
        self.valor = valor
        self.palo = palo
        
    def __str__(self) :
        return "Cartita: " + str(self.valor.name) + " de " + str(self.palo.name)