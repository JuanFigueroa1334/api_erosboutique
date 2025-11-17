from src.database.db import get_connection
from .entities.Opinion import Opinion

class opinionModel():
    @classmethod
    def get_opiniones(self):
        try:
            connection=get_connection()
            opiniones = []
            with connection.cursor() as cursor:
                cursor.execute("SELECT id, usuario_id, descripcion, fecha_creacion, calificacion FROM opinion_tienda")
                resultset=cursor.fetchall()
                for row in resultset:
                    opinion = Opinion(row[0], row[1], row[2],row[3],row[4])
                    opiniones.append(opinion.to_JSON())
                    
            connection.close()
            return opiniones 
        except Exception as ex:
            raise Exception(ex)
        
    @classmethod
    def get_opinion(self,id):
        try:
            connection=get_connection()

            with connection.cursor() as cursor:
                cursor.execute("SELECT id, usuario_id, descripcion, fecha_creacion, calificacion FROM opinion_tienda WHERE id = %s",(id,))
                row=cursor.fetchone()
                opinion=None
                if row != None:
                    opinion = Opinion(row[0], row[1], row[2], row[3], row[4])
                    opinion = opinion.to_JSON()
            connection.close()
            return opinion
        except Exception as ex:
            raise Exception(ex)
    
    @classmethod
    def add_opinion(self,opinion):
        try:
            connection=get_connection()

            with connection.cursor() as cursor:
                cursor.execute("""INSERT INTO opinion_tienda (usuario_id, descripcion, fecha_creacion, calificacion) 
                               VALUES ( %s, %s, %s, %s)""",
                               (opinion.usuario_id, opinion.descripcion, opinion.fecha_creacion, opinion.calificacion))
                affected_rows = cursor.rowcount
                connection.commit()                
            connection.close()
            return affected_rows
        except Exception as ex:
            raise Exception(ex)
        
    @classmethod
    def update_opinion(self,opinion):
        try:
            connection=get_connection()

            with connection.cursor() as cursor:
                cursor.execute("""UPDATE opinion_tienda SET usuario_id=%s, descripcion=%s, fecha_creacion=%s, calificacion=%s
                               WHERE id=%s""",
                               (opinion.usuario_id, opinion.descripcion, opinion.fecha_creacion, opinion.calificacion,opinion.id))
                affected_rows = cursor.rowcount
                connection.commit()                
            connection.close()
            return affected_rows
        except Exception as ex:
            raise Exception(ex)
        
    @classmethod
    def delete_opinion(self,id):
        try:
            connection=get_connection()

            with connection.cursor() as cursor:
                cursor.execute("DELETE FROM opinion_tienda WHERE id = %s", (id,))
                affected_rows = cursor.rowcount
                connection.commit()                
            connection.close()
            return affected_rows
        except Exception as ex:
            raise Exception(ex)