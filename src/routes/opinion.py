from flask import Blueprint, jsonify, request

from src.models.entities.Opinion import Opinion
from src.models.opinionModel import opinionModel

main = Blueprint('opinion_blueprint', __name__)

@main.route('/')
def get_opiniones():
    try:
        opiniones=opinionModel.get_opiniones()
        return jsonify(opiniones)
    except Exception as ex:
        return jsonify({'message': str(ex)}),500
    
@main.route('/<id>')
def get_opinion(id):
    try:
        opinion = opinionModel.get_opinion(id)
        if opinion != None:
            return jsonify(opinion)
        else:
            return jsonify({}),404
    except Exception as ex:
        return jsonify({'message': str(ex)}),500
    
@main.route('/add', methods=['POST'])
def add_opinion():
    try:
        usuario_id = request.json['usuario_id']
        descripcion = request.json['descripcion']
        fecha_creacion = request.json['fecha_creacion']
        calificacion = request.json['calificacion']
        
        opini = Opinion(None,usuario_id,descripcion,fecha_creacion,calificacion)
        affected_rows = opinionModel.add_opinion(opini)
        if affected_rows == 1:
            return jsonify({'message':"Opinion insertada"}), 200
        else:
            return jsonify({'message':"Error on insert"}), 500
    except Exception as ex:
        return jsonify({'message': str(ex)}),500
    
@main.route('/update/<id>', methods=['PUT'])
def update_opinion(id):
    try:
        usuario_id = request.json['usuario_id']
        descripcion = request.json['descripcion']
        fecha_creacion = request.json['fecha_creacion']
        calificacion = request.json['calificacion']
        
        opini = Opinion(id,usuario_id,descripcion,fecha_creacion,calificacion)
        affected_rows = opinionModel.update_opinion(opini)
        if affected_rows == 1:
            return jsonify({
                'message': f"Usuario '{opini.usuario_id}' actualizo opinion con id '{opini.id}'",
                'id': opini.id
            }), 200
        else:
            return jsonify({'message':"Error on update!"}), 404
    except Exception as ex:
        return jsonify({'message': str(ex)}),500
    
@main.route('/delete/<id>', methods=['DELETE'])
def delete_opinion(id):
    try:
        affected_rows = opinionModel.delete_opinion(id)
        if affected_rows == 1:
            return jsonify({
                        "message": f"Opinion con ID {id} eliminada correctamente."
                    }), 200
        else:
            return jsonify({'message':"no user delete!"}), 404
    except Exception as ex:
        return jsonify({'message': str(ex)}),500