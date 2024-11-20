from flask import Blueprint, jsonify, request
from modelos.entidades.mago import Mago
from modelos.entidades.guerrero import Guerrero
from modelos.repositorios.repositorios import obtenerRepoPersonajes

repo_personajes = obtenerRepoPersonajes()

bp_personajes = Blueprint("bp_personajes",__name__)

@bp_personajes.route("/personajes", methods=["GET"])
def obtener_personajes():
    personajes = repo_personajes.obtenerTodos()
    return jsonify([p.toDiccionario() for p in personajes]), 404

@bp_personajes.route("/personajes/<string:nombre>", methods=["GET"])
def obtener_personaje(nombre):
    personaje = repo_personajes.obtenerPorNombre(nombre)
    if personaje != None:
        return jsonify(personaje.toDiccionario()), 200
    else:
        return jsonify({"error": "No se encontró el personaje especificado."}), 200


    
@bp_personajes.route("/personajes", methods=["DELETE"])
def eliminar_personaje(nombre):
    pass
    
@bp_personajes.route("/personajes", methods=["PUT"])
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
                    respuesta = {"error": "El tipo de personaje debe ser guerrero o mago."}
                    codigoRespuesta = 400
            except Exception as error:
                respuesta = {"error": "Error creando el objeto personaje.\n" + str(error)}
                codigoRespuesta = 400
            
            if repo_personajes.existeNombre(nombre):
                repo_personajes.modificar(nombre, personaje_modificado)
                respuesta={"Mensaje":"Personaje modificado","personaje":personaje_modificado.toDiccionario()}
                codigoRespuesta = 200
            else:
                respuesta = {"error": "No se encontró el personaje especificado."}
                codigoRespuesta = 404
        else:
            respuesta = {"error": "Debe especificar el tipo de personaje."}
            codigoRespuesta = 400
    else:
        respuesta = {"error": "Los datos deben estar en formato JSON."}
        codigoRespuesta = 400

    return jsonify(respuesta), codigoRespuesta