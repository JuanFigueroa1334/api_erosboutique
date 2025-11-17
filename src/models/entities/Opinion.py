from src.utils.DateFormat import DateFormat
class Opinion():
    def __init__(self, id=None, usuario_id=None, descripcion=None, fecha_creacion=None, calificacion=None):
        self.id = id
        self.usuario_id = usuario_id
        self.descripcion = descripcion
        self.fecha_creacion = fecha_creacion
        self.calificacion = calificacion

    def to_JSON(self):
        return {
            'id': self.id,
            'usuario_id': self.usuario_id,
            'descripcion': self.descripcion,
            'fecha_creacion': self.fecha_creacion,
            'calificacion': self.calificacion,
        }