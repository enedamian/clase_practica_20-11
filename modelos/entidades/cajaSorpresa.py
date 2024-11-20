import random
from enum import Enum

class Caracteristica(Enum):
    VIDA = "vida"
    ATAQUE = "ataque"
    DEFENSA = "defensa"


class CajaSorpresa:
    def __init__(self):
        """Inicializa una caja sorpresa con valores aleatorios de vida, ataque y defensa."""
        self.__caracteristica = random.choice(list(Caracteristica))
        self.__valor = random.randint(-10,20)

    def obtenerCaracteristica(self)->Caracteristica:
        """Devuelve la característica de la caja sorpresa."""
        return self.__caracteristica
    
    def obtenerValor(self)->int:
        """Devuelve el valor de la caja sorpresa."""
        return self.__valor
    
    def deshabilitarCaja(self):
        """Deshabilita la caja sorpresa."""
        self.__caracteristica = None
        self.__valor = None