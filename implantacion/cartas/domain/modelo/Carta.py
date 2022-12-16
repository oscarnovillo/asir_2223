from enum import Enum
from dataclasses import dataclass,field


@dataclass(order=True)
class Carta:
    
    
    class PALOS(Enum):
        OROS = 1
        ESPADAS = 2
        COPAS = 3
        BASTOS = 4

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
