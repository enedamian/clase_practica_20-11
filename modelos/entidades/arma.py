class Arma:
    @classmethod
    def fromDiccionario(cls, diccionario: dict):
        """Crea un arma a partir de un diccionario."""
        return Arma(diccionario["nombre"], diccionario["tipo"], diccionario["danio"])

    def __init__(self, nombre:str, tipo:str, danio:int):
        if not isinstance(nombre, str) or nombre == "" or nombre.isspace():
            raise ValueError("El nombre debe ser un string válido.")
        if not isinstance(tipo, str) or tipo == "" or tipo.isspace():
            raise ValueError("El tipo debe ser un string válido.")
        if not isinstance(danio, int) or danio < 0:
            raise ValueError("El daño debe ser un número entero positivo.")
        self.__nombre = nombre
        self.__tipo = tipo
        self.__danio = danio

    def obtenerNombre(self):
        return self.__nombre
    
    def obtenerTipo(self):
        return self.__tipo
    
    def obtenerDanio(self):
        return self.__danio

    def __str__(self):
        return f"{self.__nombre} - {self.__tipo} (+{self.__danio} de daño)"
    
    def clonar(self):
        return Arma(self.__nombre, self.__tipo, self.__danio)
    
    def esIgual(self, otra_arma:"Arma")->bool:
        """Determina si una arma es igual a otra. Si no recibe un objeto de tipo Arma lanza un ValueError."""
        if not isinstance(otra_arma, Arma):
            raise ValueError("El objeto a comparar debe ser de tipo Arma.")
        return self.__nombre == otra_arma.obtenerNombre() and self.__tipo == otra_arma.obtenerTipo() and self.__danio == otra_arma.obtenerDanio()
    
    def copiarValores(self, otra_arma:"Arma"):
        """Copia los valores de otra arma en la actual. Si no recibe un objeto de tipo Arma lanza un ValueError."""
        if not isinstance(otra_arma, Arma):
            raise ValueError("El objeto a comparar debe ser de tipo Arma.")
        self.__nombre = otra_arma.obtenerNombre()
        self.__tipo = otra_arma.obtenerTipo()
        self.__danio = otra_arma.obtenerDanio()

    def toDiccionario(self):
        return {
            "nombre": self.__nombre,
            "tipo": self.__tipo,
            "danio": self.__danio
        }