from modelos.entidades.arma import Arma   # Importamos la clase Arma desde el archivo Arma.py
from modelos.entidades.cajaSorpresa import CajaSorpresa, Caracteristica   # Importamos la clase CajaSorpresa desde el archivo CajaSorpresa.py

class Personaje:
    MAX_VIDA = 100
    MAX_ATAQUE = 50
    MAX_DEFENSA = 45
    MIN_VIDA = 0
    MIN_ATAQUE = 5
    MIN_DEFENSA = 0

    def __init__(self, nombre:str, ataque:int, defensa:int):
        """
        Inicializa un nuevo personaje con el maximo de vida.
        
        Parámetros:
        - nombre: El nombre del personaje.
        - ataque: La cantidad de ataque del personaje.
        - defensa: La cantidad de defensa del personaje.
        """
        if not isinstance(nombre, str) or nombre == "" or nombre.isspace():
            raise ValueError("El nombre debe ser un string válido.")
        if not isinstance(ataque, int) or ataque < Personaje.MIN_ATAQUE or ataque > Personaje.MAX_ATAQUE:
            raise ValueError(f"El ataque debe ser un número entero entre {Personaje.MIN_ATAQUE} y {Personaje.MAX_ATAQUE}.")
        if not isinstance(defensa, int) or defensa < Personaje.MIN_DEFENSA or defensa > Personaje.MAX_DEFENSA:
            raise ValueError(f"La defensa debe ser un número entero entre {Personaje.MIN_DEFENSA} y {Personaje.MAX_DEFENSA}.")
        self._nombre=nombre
        self._vida = Personaje.MAX_VIDA
        self._ataque=ataque
        self._defensa=defensa
        self._arma=None
    
    #consultas triviales
    def obtenerNombre(self)->str:
        """Devuelve el nombre del personaje."""
        return self._nombre
    
    def obtenerVida(self)->int:
        """Devuelve la vida del personaje."""
        return self._vida
    
    def obtenerAtaque(self)->int:
        """Devuelve el ataque del personaje."""
        return self._ataque
    
    def obtenerDefensa(self)->int:
        """Devuelve la defensa del personaje."""
        return self._defensa
    
    def obtenerArma(self)->Arma:
        """Devuelve el arma del personaje."""
        return self._arma
    
    def __str__(self)->str:
        """Devuelve una representación de string del personaje."""
        return f"Nombre: {self._nombre}, Vida: {self._vida}, Ataque: {self._ataque}, Defensa: {self._defensa}, Arma: {self._arma if self._arma!=None else 'Ninguna'}"
    
    #consultas
    def estaVivo(self):
        """Devuelve True si el personaje está vivo."""
        return self._vida>0
    
    #clonación superficial
    def clonarSup(self)->"Personaje":
        """Devuelve un clon del personaje."""
        clon = Personaje(self._nombre, self._ataque, self._defensa)
        clon.establecerVida(self._vida)
        clon.establecerArma(self._arma)
        return clon
            
    #clonación en profundidad
    def clonarProf(self)->"Personaje":
        """Devuelve un clon en profundidad del personaje."""
        clon = Personaje(self._nombre, self._ataque, self._defensa)
        clon.establecerVida(self._vida)
        if self._arma!=None:
            clon.establecerArma(self._arma.clonar())
        return clon
    
    #igualdad superficial
    def esIgualSup(self, otro:"Personaje")->bool:
        """Devuelve True si el personaje es igual a otro, False en caso contrario. Retorna ValueError si otro no es un objeto de la clase Personaje."""
        if isinstance(otro, Personaje):
            return self._nombre==otro.obtenerNombre() and self._vida==otro.obtenerVida() and self._ataque==otro.obtenerAtaque() and self._defensa==otro.obtenerDefensa() and self._arma==otro.obtenerArma()
        else:
            raise ValueError("El personaje a comparar debe ser un objeto de la clase Personaje.")
        
    #igualdad en profundidad
    def esIgualProf(self, otro:"Personaje")->bool:
        """Devuelve True si el personaje es igual a otro, False en caso contrario. Retorna ValueError si otro no es un objeto de la clase Personaje."""
        if isinstance(otro, Personaje):
            return self._nombre==otro.obtenerNombre() and self._vida==otro.obtenerVida() and self._ataque==otro.obtenerAtaque() and self._defensa==otro.obtenerDefensa() and self._arma.esIgual(otro.obtenerArma())
        else:
            raise ValueError("El personaje a comparar debe ser un objeto de la clase Personaje.")

    
    #comandos triviales
    def establecerVida(self, vida:int):
        """Establece la vida del personaje. Si el valor de vida no es un número entero, se lanza un ValueError."""
        if isinstance(vida, int):
            if vida>=Personaje.MIN_VIDA and vida<=Personaje.MAX_VIDA:
                self._vida=vida
        else:
            raise ValueError("El valor de vida debe ser un número entero.")

    def establecerAtaque(self, ataque:int):
        """Establece el ataque del personaje. Si el valor de ataque no es un número entero, se lanza un ValueError."""
        if isinstance(ataque, int):
            if ataque>=Personaje.MIN_ATAQUE and ataque<=Personaje.MAX_ATAQUE:
                self._ataque=ataque
        else:
            raise ValueError("El valor de ataque debe ser un número entero positivo.")

    def establecerDefensa(self, defensa:int):
        """Establece la defensa del personaje. Si el valor de defensa no es un número entero, se lanza un ValueError."""
        if isinstance(defensa, int):
            if defensa>=Personaje.MIN_DEFENSA and defensa<=Personaje.MAX_DEFENSA:
                self._defensa=defensa
        else:
            raise ValueError("El valor de defensa debe ser un número entero positivo.")
    
    def establecerArma(self, arma:Arma):
        """Establece el arma del personaje. Si el valor de arma no es un objeto de la clase Arma, se lanza un ValueError."""
        if isinstance(arma, Arma):
            self._arma = arma
        else:
            raise ValueError("El arma debe ser un objeto de la clase Arma.")

    #comandos
    def atacar(self, otro_personaje:"Personaje"):
        """
        Ataca a otro personaje.
        Requiere que otro_personaje esté ligado a un objeto Personaje (no sea None).
        Si no recibe un objeto de la clase Personaje, lanza un ValueError.
        """
        if isinstance(otro_personaje, Personaje):
            if self.estaVivo():
                if self._arma!=None:
                    # Si el personaje tiene un arma, se suma el daño del arma al ataque
                    otro_personaje.recibirAtaque(self._ataque+self._arma.obtenerDanio())
                else:
                    otro_personaje.recibirAtaque(self._ataque)
        else:
            raise ValueError("El personaje a atacar debe ser un objeto de la clase Personaje.")

    def recibirAtaque(self, valorAtaque:int):
        """Recibe un ataque y ajusta la vida del personaje. Si el valor de ataque no es un número entero, se lanza un ValueError."""
        if isinstance(valorAtaque, int):
            if self.estaVivo():
                if self._defensa < valorAtaque:
                    # Si la defensa del personaje es menor al ataque recibido, 
                    # se resta la diferencia a la vida del personaje
                    if self._vida - (valorAtaque-self._defensa) <= 0:
                        self._vida = Personaje.MIN_VIDA
                    else:
                        self._vida -= (valorAtaque-self._defensa)
        else:
            raise ValueError("El valor de ataque debe ser un número entero positivo.")

    def abrirCaja(self, caja: CajaSorpresa):
        """Abre una caja sorpresa y ajusta los atributos del personaje."""
        if isinstance(caja, CajaSorpresa) and self.estaVivo():
            if caja.obtenerCaracteristica() == Caracteristica.VIDA:
                if self._vida + caja.obtenerValor() > Personaje.MAX_VIDA:
                    self._vida = Personaje.MAX_VIDA
                elif self._vida + caja.obtenerValor() < Personaje.MIN_VIDA:
                    self._vida = Personaje.MIN_VIDA
                else:
                    self._vida += caja.obtenerValor()
            elif caja.obtenerCaracteristica() == Caracteristica.ATAQUE:
                if self._ataque + caja.obtenerValor() > Personaje.MAX_ATAQUE:
                    self._ataque = Personaje.MAX_ATAQUE
                elif self._ataque + caja.obtenerValor() < Personaje.MIN_ATAQUE:
                    self._ataque = Personaje.MIN_ATAQUE
                else:
                    self._ataque += caja.obtenerValor()
            elif caja.obtenerCaracteristica() == Caracteristica.DEFENSA:
                if self._defensa + caja.obtenerValor() > Personaje.MAX_DEFENSA:
                    self._defensa = Personaje.MAX_DEFENSA
                elif self._defensa + caja.obtenerValor() < Personaje.MIN_DEFENSA:
                    self._defensa = Personaje.MIN_DEFENSA
                else:
                    self._defensa += caja.obtenerValor()

    #copia superficial
    def copiarValoresSup(self, otro:"Personaje"):
        """Copia los valores de otro personaje. Si otro no es un objeto de la clase Personaje, lanza un ValueError."""
        if isinstance(otro, Personaje):
            self._nombre = otro.obtenerNombre()
            self._vida = otro.obtenerVida()
            self._ataque = otro.obtenerAtaque()
            self._defensa = otro.obtenerDefensa()
            self._arma = otro.obtenerArma()
        else:
            raise ValueError("El personaje a copiar debe ser un objeto de la clase Personaje.")
        
    #copia en profundidad
    def copiarValoresProf(self, otro:"Personaje"):
        """Copia en profundidad los valores de otro personaje. Si otro no es un objeto de la clase Personaje, lanza un ValueError."""
        if isinstance(otro, Personaje):
            self._nombre = otro.obtenerNombre()
            self._vida = otro.obtenerVida()
            self._ataque = otro.obtenerAtaque()
            self._defensa = otro.obtenerDefensa()
            if otro.obtenerArma()!=None:
                if self._arma!=None:
                    self._arma.copiarValores(otro.obtenerArma())
                else:
                    self._arma = otro.obtenerArma().clonar()
            else:
                self._arma = None
        else:
            raise ValueError("El personaje a copiar debe ser un objeto de la clase Personaje.")
    
