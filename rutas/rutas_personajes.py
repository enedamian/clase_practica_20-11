from flask import Blueprint, jsonify, request

from modelos.entidades.mago import Mago
from modelos.entidades.guerrero import Guerrero
from modelos.repositorios.repositorios import obtenerRepoPersonajes

repo_personajes = obtenerRepoPersonajes()

bp_personajes = Blueprint("bp_personajes",__name__)

@bp_personajes.route("/personajes", methods=["GET"])
def obtener_personajes():
    personajes = repo_personajes.obtenerTodos()
    return jsonify([p.toDiccionario() for p in personajes])

@bp_personajes.route("/personajes/<string:nombre>", methods=["GET"])
def obtener_personaje(nombre):
    personaje = repo_personajes.obtenerPorNombre(nombre)
    if personaje != None:
        return jsonify(personaje.toDiccionario()), 200
    else:
        return jsonify({"error": "No se encontró el personaje especificado."}), 404

@bp_personajes.route("/personajes", methods=["POST"])
def agregar_personaje():
    if request.is_json:
        datos = request.get_json()
        if "tipo" in datos:
            try:
                if datos["tipo"] == "guerrero":
                    nuevo_personaje = Guerrero.fromDiccionario(datos)
                elif datos["tipo"] == "mago":
                    nuevo_personaje = Mago.fromDiccionario(datos)
                else:
                    return jsonify({"error": "El tipo de personaje debe ser guerrero o mago."}), 400
            except Exception as error:
                return jsonify({"error": "Error creando el objeto personaje.\n" + str(error)}), 400
            print(nuevo_personaje)
            if not repo_personajes.existeNombre(nuevo_personaje):
                repo_personajes.agregar(nuevo_personaje)
                return jsonify(nuevo_personaje.toDiccionario()), 201
            else:
                return jsonify({"error": "Ya existe un personaje con el mismo nombre."}), 400
        else:
            return jsonify({"error": "Debe especificar el tipo de personaje."}), 400
        
    else:
        return jsonify({"error": "Los datos deben estar en formato JSON."}), 400
    
@bp_personajes.route("/personajes/<string:nombre>", methods=["DELETE"])
def eliminar_personaje(nombre):
    if repo_personajes.existeNombre(nombre):
        repo_personajes.eliminar(nombre)
        return jsonify({"mensaje": "Personaje eliminado."}), 200
    else:
        return jsonify({"error": "No se encontró el personaje especificado."}), 404
    
@bp_personajes.route("/personajes/<string:nombre>", methods=["PUT"])
def modificar_personaje(nombre):
    if request.is_json:
        datos = request.get_json()
        if "tipo" in datos:
            try:
                if datos["tipo"] == "guerrero":
                    personaje_modificado = Guerrero.fromDiccionario(datos)
                elif datos["tipo"] == "mago":
                    personaje_modificado = Mago.fromDiccionario(datos)
                else:
                    return jsonify({"error": "El tipo de personaje debe ser guerrero o mago."}), 400
            except Exception as error:
                return jsonify({"error": "Error creando el objeto personaje.\n" + str(error)}), 400
            
            if repo_personajes.existeNombre(nombre):
                repo_personajes.modificar(nombre, personaje_modificado)
                return jsonify(personaje_modificado.toDiccionario()), 200
            else:
                return jsonify({"error": "No se encontró el personaje especificado."}), 404
        else:
            return jsonify({"error": "Debe especificar el tipo de personaje."}), 400
    else:
        return jsonify({"error": "Los datos deben estar en formato JSON."}), 400