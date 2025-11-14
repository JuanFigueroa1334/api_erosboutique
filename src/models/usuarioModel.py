from src.database.db import get_connection
from .entities.User import User

class usuarioModel():
    @classmethod
    def get_usuarios(self):
        try:
            connection=get_connection()
            usuarios = []
            with connection.cursor() as cursor:
                cursor.execute("SELECT id, nombre, apellidos, usuario, clave, perfil, fecha_nacimiento, genero, correo, contacto, direccion FROM usuario ORDER BY nombre ASC")
                resultset=cursor.fetchall()
                for row in resultset:
                    user = User(row[0], row[1], row[2],row[3],row[4],row[5],row[6],row[7],row[8],row[9],row[10])
                    usuarios.append(user.to_JSON())
                    
            connection.close()
            return usuarios 
        except Exception as ex:
            raise Exception(ex)
        
   