from src.database.db import get_connection
from src.models.entities.Producto import Producto
from src.models.entities.ProductImages import ProductoImages

class ProductoModel():

    # -----------------------------------------------------------
    # GET ALL PRODUCTOS (CON IMÁGENES)
    # -----------------------------------------------------------
    @classmethod
    def get_productos(cls):
        try:
            connection = get_connection()
            productos = []
            with connection.cursor() as cursor:
                cursor.execute("""
                    SELECT id, nombre, descripcion, precio, costo, marca, stock
                    FROM producto ORDER BY nombre ASC
                """)
                rows = cursor.fetchall()

                for row in rows:
                    producto = Producto(*row).to_JSON()

                    cursor.execute("""
                        SELECT id, producto_id, url_imagen
                        FROM producto_imagen
                        WHERE producto_id = %s
                    """, (row[0],))
                    imagenes = cursor.fetchall()

                    producto["imagenes"] = [
                        ProductoImages(*img).to_JSON() for img in imagenes
                    ]

                    productos.append(producto)

            connection.close()
            return productos

        except Exception as ex:
            raise Exception(ex)

    # -----------------------------------------------------------
    # GET PRODUCTO BY ID
    # -----------------------------------------------------------
    @classmethod
    def get_producto(cls, id):
        try:
            connection = get_connection()
            with connection.cursor() as cursor:
                cursor.execute("""
                    SELECT id, nombre, descripcion, precio, costo, marca, stock
                    FROM producto
                    WHERE id = %s
                """, (id,))
                row = cursor.fetchone()

                if row is None:
                    return None

                producto = Producto(*row).to_JSON()

                cursor.execute("""
                    SELECT id, producto_id, url_imagen
                    FROM producto_imagen
                    WHERE producto_id = %s
                """, (id,))
                imagenes = cursor.fetchall()

                producto["imagenes"] = [
                    ProductoImages(*img).to_JSON() for img in imagenes
                ]

            connection.close()
            return producto

        except Exception as ex:
            raise Exception(ex)

    # -----------------------------------------------------------
    # INSERT PRODUCTO + IMÁGENES
    # -----------------------------------------------------------
    @classmethod
    def add_producto(cls, producto, imagenes):
        try:
            connection = get_connection()
            with connection.cursor() as cursor:
                cursor.execute("""
                    INSERT INTO producto (nombre, descripcion, precio, costo, marca, stock)
                    VALUES (%s, %s, %s, %s, %s, %s)
                    RETURNING id
                """, (producto.nombre, producto.descripcion, producto.precio,
                      producto.costo, producto.marca, producto.stock))

                new_id = cursor.fetchone()[0]

                # Insertar imágenes
                for item  in imagenes:
                    cursor.execute("""
                        INSERT INTO producto_imagen (producto_id, url_imagen)
                        VALUES (%s, %s)
                    """, (new_id, item["url_imagen"]))

                connection.commit()
            connection.close()
            return new_id

        except Exception as ex:
            raise Exception(ex)

    # -----------------------------------------------------------
    # UPDATE PRODUCTO + IMÁGENES
    # -----------------------------------------------------------
    @classmethod
    def update_producto(cls, producto, imagenes):
        try:
            connection = get_connection()
            with connection.cursor() as cursor:
                cursor.execute("""
                    UPDATE producto
                    SET nombre=%s, descripcion=%s, precio=%s, costo=%s, marca=%s, stock=%s
                    WHERE id=%s
                """, (producto.nombre, producto.descripcion, producto.precio,
                      producto.costo, producto.marca, producto.id, producto.stock))

                # Eliminar imágenes anteriores
                cursor.execute("""
                    DELETE FROM producto_imagen WHERE producto_id = %s
                """, (producto.id,))

                # Insertar nuevas imágenes
                for item in imagenes:
                    cursor.execute("""
                        INSERT INTO producto_imagen (producto_id, url_imagen)
                        VALUES (%s, %s)
                    """, (producto.id, item["url_imagen"]))

                affected = cursor.rowcount
                connection.commit()

            connection.close()
            return affected

        except Exception as ex:
            raise Exception(ex)

    # -----------------------------------------------------------
    # DELETE PRODUCTO + SUS IMÁGENES
    # -----------------------------------------------------------
    @classmethod
    def delete_producto(cls, id):
        try:
            connection = get_connection()
            with connection.cursor() as cursor:

                cursor.execute("""
                    DELETE FROM producto_imagen WHERE producto_id = %s
                """, (id,))

                cursor.execute("""
                    DELETE FROM producto WHERE id = %s
                """, (id,))

                affected_rows = cursor.rowcount
                connection.commit()

            connection.close()
            return affected_rows

        except Exception as ex:
            raise Exception(ex)
