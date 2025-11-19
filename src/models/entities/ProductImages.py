from src.utils.DateFormat import DateFormat
class ProductoImages():
    def __init__(self, id=None, producto_id=None, url_imagen=None):
        self.id = id
        self.producto_id = producto_id
        self.url_imagen = url_imagen

    def to_JSON(self):
        return {
            'id': self.id,
            'producto_id': self.producto_id,
            'url_imagen': self.url_imagen,
        }