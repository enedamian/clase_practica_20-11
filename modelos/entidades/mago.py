from modelos.entidades.personaje import Personaje
from modelos.entidades.arma import Arma
import random

class Mago(Personaje):
    MAX_MANA=100
    PORCENTAJE_AUMENTO_ATAQUE=0.3


    def __init__(self, nombre:str, ataque:int, defensa:int):
        """Inicializa los atributos de un mago."""
        super().__init__(nombre, ataque, defensa)
        self.__mana =  Mago.MAX_MANA

    def obtenerMana(self)->int:
        """Devuelve el mana del mago."""
        return self.__mana
    
    def establecerMana(self, mana:int):
        """Establece el mana del mago."""
        if not isinstance(mana, int) or mana < 0:
            raise ValueError("El mana debe ser un número entero positivo.")
        self.__mana = mana
    
    def lanzarHechizo(self, enemigo:Personaje):
        """Lanza un hechizo al enemigo especificado. Consume 10 puntos de mana.
        Si no recibe un personaje lanza un ValueError.
        """
        if not isinstance(enemigo, Personaje):
            raise ValueError("El enemigo no puede ser None.")
        if self.estaVivo():
            if self.__mana >= 10:
                enemigo.recibirAtaque(int(self._ataque * (1 + Mago.PORCENTAJE_AUMENTO_ATAQUE)))
                self.__mana -= 10
            else:
                raise ValueError("El mago no tiene suficiente mana para lanzar un hechizo.")
            
    def recibirAtaque(self, valorAtaque: int):
        """Recibe un ataque del enemigo.
        Aleatoriamente el mago puede repeler el ataque y no recibir daño.
        Si no puede repelerlo recibe el daño normalmente.
        """
        # si el numero aleatorio es par, recibe el ataque
        if random.randint(1,10) % 2 == 0:
            super().recibirAtaque(valorAtaque)
        else:
            print(f"{self._nombre} ha repelido el ataque.")

    def __str__(self) -> str:
        return f"{super().__str__()}, Mana: {self.__mana}"

