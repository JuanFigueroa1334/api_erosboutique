from src.utils.DateFormat import DateFormat
class User():
    def __init__(self, id, nombre=None, apellidos=None, usuario=None, clave=None, perfil=None, 
                 fecha_nacimiento=None, genero=None, correo=None, contacto=None, direccion=None):
        self.id = id
        self.nombre = nombre
        self.apellidos = apellidos
        self.usuario = usuario
        self.clave = clave
        self.perfil = perfil
        self.fecha_nacimiento = fecha_nacimiento
        self.genero = genero
        self.correo = correo
        self.contacto = contacto
        self.direccion = direccion
        
    def to_JSON(self):
        return {
            'id': self.id,
            'nombre': self.nombre,
            'apellidos': self.apellidos,
            'usuario': self.usuario,
            'clave': self.clave,
            'perfil': self.perfil,
            'fecha_nacimiento': DateFormat.convert_date(self.fecha_nacimiento),
            'genero': self.genero,
            'correo': self.correo,
            'contacto': self.contacto,
            'direccion': self.direccion
        }
        