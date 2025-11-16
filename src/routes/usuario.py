from flask import Blueprint, jsonify, request

from src.models.entities.User import User
from src.models.usuarioModel import usuarioModel

main = Blueprint('usuario_blueprint', __name__)

@main.route('/')
def get_users():
    try:
        usuarios=usuarioModel.get_usuarios()
        return jsonify(usuarios)
    except Exception as ex:
        return jsonify({'message': str(ex)}),500
    
@main.route('/<id>')
def get_user(id):
    try:
        user = usuarioModel.get_usuario(id)
        if user != None:
            return jsonify(user)
        else:
            return jsonify({}),404
    except Exception as ex:
        return jsonify({'message': str(ex)}),500
    
@main.route('/add', methods=['POST'])
def add_user():
    try:
        nombre = request.json['nombre']
        apellidos = request.json['apellidos']
        usuario = request.json['usuario']
        clave = request.json['clave']
        perfil = request.json['perfil']
        fecha_nacimiento = request.json['fecha_nacimiento']
        genero = request.json['genero']
        correo = request.json['correo']
        contacto = request.json['contacto']
        direccion = request.json['direccion']
        
        user = User(None,nombre,apellidos,usuario,clave,perfil,fecha_nacimiento,genero,correo,contacto,direccion)
        affected_rows = usuarioModel.add_usuario(user)
        if affected_rows == 1:
            return jsonify({'message':"Usuario insertado"}), 200
        else:
            return jsonify({'message':"Error on insert"}), 500
    except Exception as ex:
        return jsonify({'message': str(ex)}),500
    
@main.route('/update/<id>', methods=['PUT'])
def update_user(id):
    try:
        nombre = request.json['nombre']
        apellidos = request.json['apellidos']
        usuario = request.json['usuario']
        clave = request.json['clave']
        perfil = request.json['perfil']
        fecha_nacimiento = request.json['fecha_nacimiento']
        genero = request.json['genero']
        correo = request.json['correo']
        contacto = request.json['contacto']
        direccion = request.json['direccion']
        
        user = User(id,nombre,apellidos,usuario,clave,perfil,fecha_nacimiento,genero,correo,contacto,direccion)
        affected_rows = usuarioModel.update_usuario(user)
        if affected_rows == 1:
            return jsonify({
                'message': f"Usuario '{user.nombre}' actualizado exitosamente",
                'id': user.id
            }), 200
        else:
            return jsonify({'message':"Error on update!"}), 404
    except Exception as ex:
        return jsonify({'message': str(ex)}),500
    
@main.route('/delete/<id>', methods=['DELETE'])
def delete_user(id):
    try:
        affected_rows = usuarioModel.delete_usuario(id)
        if affected_rows == 1:
            return jsonify({
                        "message": f"Usuario con ID {id} eliminado correctamente."
                    }), 200
        else:
            return jsonify({'message':"no user delete!"}), 404
    except Exception as ex:
        return jsonify({'message': str(ex)}),500
#login
@main.route('/login', methods=['POST'])
def login():
    try:
        usuario = request.json['usuario']
        clave = request.json['clave']

        user = usuarioModel.login(usuario, clave)

        if user:
            return jsonify({
                "id": user.id,
                "usuario": user.usuario,
                "perfil": user.perfil
            }), 200
        else:
            return jsonify({"message": "Credenciales incorrectas"}), 401

    except Exception as ex:
        return jsonify({'message': str(ex)}), 500