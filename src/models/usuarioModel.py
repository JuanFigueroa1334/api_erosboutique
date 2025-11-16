from database.db import get_connection
from .entities.User import usuario

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
                    user = usuario(row[0], row[1], row[2],row[3],row[4],row[5],row[6],row[7],row[8],row[9],row[10])
                    usuarios.append(user.to_JSON())
                    
            connection.close()
            return usuarios 
        except Exception as ex:
            raise Exception(ex)
        
    @classmethod
    def get_usuario(self,id):
        try:
            connection=get_connection()

            with connection.cursor() as cursor:
                cursor.execute("SELECT id, nombre, apellidos, usuario, clave, perfil, fecha_nacimiento, genero, correo, contacto, direccion FROM usuario WHERE id = %s",(id,))
                row=cursor.fetchone()
                user=None
                if row != None:
                    user = usuario(row[0], row[1], row[2],row[3],row[4],row[5],row[6],row[7],row[8],row[9],row[10])
                    user = user.to_JSON()
            connection.close()
            return user
        except Exception as ex:
            raise Exception(ex)
        
    @classmethod
    def add_usuario(self,user):
        try:
            connection=get_connection()

            with connection.cursor() as cursor:
                cursor.execute("""INSERT INTO usuario (id, nombre, apellidos, usuario, clave, perfil, fecha_nacimiento, genero, correo, contacto, direccion) 
                               VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s,)""",
                               (user.id, user.nombre,user.apellidos,user.usuario,user.clave,user.perfil,user.fecha_nacimiento,user.genero,user.correo,user.contacto,user.direccion))
                affected_rows = cursor.rowcount
                connection.commit()                
            connection.close()
            return affected_rows
        except Exception as ex:
            raise Exception(ex)
        
    @classmethod
    def update_usuario(self,user):
        try:
            connection=get_connection()

            with connection.cursor() as cursor:
                cursor.execute("""UPDATE usuario SET nombre=%s, apellidos=%s, usuario=%s, clave=%s, perfil=%s, fecha_nacimiento=%s, genero=%s, correo=%s, contacto=%s, direccion=%s
                               WHERE id=%s""",
                               (user.nombre,user.apellidos,user.usuario,user.clave,user.perfil,user.fecha_nacimiento,user.genero,user.correo,user.contacto,user.direccion,user.id))
                affected_rows = cursor.rowcount
                connection.commit()                
            connection.close()
            return affected_rows
        except Exception as ex:
            raise Exception(ex)
    
    @classmethod
    def delete_usuario(self,id):
        try:
            connection=get_connection()

            with connection.cursor() as cursor:
                cursor.execute("DELETE FROM usuario WHERE ID = %s", (id,))
                affected_rows = cursor.rowcount
                connection.commit()                
            connection.close()
            return affected_rows
        except Exception as ex:
            raise Exception(ex)