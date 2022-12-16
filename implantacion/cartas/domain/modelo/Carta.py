from dataclasses import dataclass, field
from enum import Enum


@dataclass(order=True)
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
        SOTA = 10
        CABALLO = 11
        REY = 12

    sorted_by = "valor.value"
    valor :NUMEROS
    palo : PALOS


    def __str__(self) :
        return "Cartita: " + str(self.valor.value) + " de " + str(self.palo.name)
