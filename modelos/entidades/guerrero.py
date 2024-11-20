from modelos.entidades.personaje import Personaje
from modelos.entidades.arma import Arma

class Guerrero(Personaje):
    DANIO_GRITO = 15


    def __init__(self, nombre:str, ataque:int, defensa:int):
        """Inicializa los atributos de un guerrero."""
        super().__init__(nombre, ataque, defensa)
        self.__gritoActivo = False

    def gritoGuerra(self):
        """Activa el grito de guerra del guerrero.
        Consume 1 punto de vida, pero le permite incrementar el ataque 15 puntos en el próximo ataque."""
        if self._vida  > 1:
            self._vida -= 1
            self.__gritoActivo = True

    def establecerGritoActivo(self, gritoActivo:bool):
        """Establece si el grito de guerra está activo."""
        if not isinstance(gritoActivo, bool):
            raise ValueError("El grito de guerra debe ser un valor booleano.")
        self.__gritoActivo = gritoActivo

    def atacar(self, enemigo:Personaje):
        """
        Ataca al enemigo especificado.
        Si no recibe un personaje lanza un ValueError.
        """
        if not isinstance(enemigo, Personaje):
            raise ValueError("El enemigo no puede ser None.")
        if self.estaVivo():
            if self.__gritoActivo:
                if self._arma != None:
                    enemigo.recibirAtaque(self._ataque + self._arma.obtenerDanio()+ Guerrero.DANIO_GRITO)
                else:
                    enemigo.recibirAtaque(self._ataque + Guerrero.DANIO_GRITO)
                self.__gritoActivo = False
            else:
                if self._arma != None:
                    enemigo.recibirAtaque(self._ataque + self._arma.obtenerDanio())
                else:
                    enemigo.recibirAtaque(self._ataque)

    def recibirAtaque(self, valorAtaque: int):
        """Recibe un ataque del enemigo."""
        if isinstance(valorAtaque, int):
            if self.estaVivo():
                if self._defensa < valorAtaque:
                    # Si la defensa del personaje es menor al ataque recibido, 
                    # reduce a la mitad el valor del daño recibido.
                    if self._vida - (valorAtaque-self._defensa)/2 <= 0:
                        self._vida = Personaje.MIN_VIDA
                    else:
                        self._vida -= int((valorAtaque-self._defensa)/2)
        else:
            raise ValueError("El valor de ataque debe ser un número entero positivo.")
