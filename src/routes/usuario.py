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
