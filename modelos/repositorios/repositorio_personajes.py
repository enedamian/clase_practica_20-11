from modelos.entidades.guerrero import Guerrero
from modelos.entidades.mago import Mago
from modelos.entidades.personaje import Personaje
import json

class RepositorioPersonajes:
    __ruta_archivo = "datos/personajes.json"

    def __init__(self):
        self.__personajes = []
        self.__cargarPersonajes()

    def __cargarPersonajes(self):
        try:
            with open(RepositorioPersonajes.__ruta_archivo, "r") as archivo:
                datos = json.load(archivo)
                for dicc_personaje in datos:
                    if dicc_personaje["tipo"] == "guerrero":
                        self.__personajes.append(Guerrero.fromDiccionario(dicc_personaje))
                    elif dicc_personaje["tipo"] == "mago":
                        self.__personajes.append(Mago.fromDiccionario(dicc_personaje))
        except FileNotFoundError:
            print("No se encontró el archivo de personajes.")
        except Exception as error:
            print(f"Error al cargar los personajes del archivo: {error}")

    def __guardarTodos(self):
        try:
            with open(RepositorioPersonajes.__ruta_archivo, "w") as archivo:
                datos = []
                for personaje in self.__personajes:
                    datos.append(personaje.toDiccionario())
                json.dump(datos, archivo, indent=4)
        except Exception as error:
            print(f"Error al guardar los personajes en el archivo: {error}")

    def obtenerTodos(self):
        return self.__personajes
    
    def obtenerPorNombre(self, nombre:str)->Personaje:
        if not isinstance(nombre, str) or nombre == "" or nombre.isspace():
            raise ValueError("El nombre debe ser un string válido.")
        for p in self.__personajes:
            if p.obtenerNombre() == nombre:
                return p
        return None
    
    def existeNombre(self, nombre):
        for p in self.__personajes:
            if p.obtenerNombre() == nombre:
                return True
        return False


    