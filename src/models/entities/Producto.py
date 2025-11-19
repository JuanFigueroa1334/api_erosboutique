from src.utils.DateFormat import DateFormat
class Producto():
    def __init__(self, id=None, nombre=None, descripcion=None, precio=None, costo=None, marca=None, stock= None):
        self.id = id
        self.nombre = nombre
        self.descripcion = descripcion
        self.precio = precio
        self.costo = costo
        self.marca = marca
        self.stock = stock

    def to_JSON(self):
        return {
            'id': self.id,
            'nombre': self.nombre,
            'descripcion': self.descripcion,
            'precio': self.precio,
            'costo': self.costo,
            'marca': self.marca,
            'stock': self.stock,
        }