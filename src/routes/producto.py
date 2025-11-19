from flask import Blueprint, jsonify, request
from src.models.entities.Producto import Producto
from src.models.productoModel import ProductoModel

main = Blueprint('producto_blueprint', __name__)

# -----------------------------------------------------------
# GET TODOS LOS PRODUCTOS
# -----------------------------------------------------------
@main.route('/')
def get_productos():
    try:
        productos = ProductoModel.get_productos()
        return jsonify(productos)
    except Exception as ex:
        return jsonify({"message": str(ex)}), 500

# -----------------------------------------------------------
# GET PRODUCTO POR ID
# -----------------------------------------------------------
@main.route('/<id>')
def get_producto(id):
    try:
        producto = ProductoModel.get_producto(id)
        if producto:
            return jsonify(producto)
        return jsonify({}), 404
    except Exception as ex:
        return jsonify({"message": str(ex)}), 500

# -----------------------------------------------------------
# INSERT PRODUCTO + IMÁGENES
# -----------------------------------------------------------
@main.route('/add', methods=['POST'])
def add_producto():
    try:
        data = request.json

        producto = Producto(
            None,
            data["nombre"],
            data["descripcion"],
            data["precio"],
            data["costo"],
            data["marca"],
            data["stock"]
        )

        imagenes = data.get("imagenes", [])

        new_id = ProductoModel.add_producto(producto, imagenes)

        return jsonify({"message": "Producto insertado", "id": new_id}), 200

    except Exception as ex:
        return jsonify({"message": str(ex)}), 500

# -----------------------------------------------------------
# UPDATE PRODUCTO + IMÁGENES
# -----------------------------------------------------------
@main.route('/update/<id>', methods=['PUT'])
def update_producto(id):
    try:
        data = request.json

        producto = Producto(
            id,
            data["nombre"],
            data["descripcion"],
            data["precio"],
            data["costo"],
            data["marca"],
            data["stock"],
        )

        imagenes = data.get("imagenes", [])

        affected = ProductoModel.update_producto(producto, imagenes)

        if affected >= 0:
            return jsonify({"message": "Producto actualizado"}), 200
        else:
            return jsonify({"message": "Error al actualizar"}), 404

    except Exception as ex:
        return jsonify({"message": str(ex)}), 500

# -----------------------------------------------------------
# DELETE PRODUCTO + SUS IMÁGENES
# -----------------------------------------------------------
@main.route('/delete/<id>', methods=['DELETE'])
def delete_producto(id):
    try:
        affected = ProductoModel.delete_producto(id)
        if affected >= 1:
            return jsonify({"message": "Producto eliminado"}), 200
        else:
            return jsonify({"message": "Producto no encontrado"}), 404

    except Exception as ex:
        return jsonify({"message": str(ex)}), 500
