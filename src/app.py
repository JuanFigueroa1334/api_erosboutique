from flask import Flask
from flask_cors import CORS
from src.config import config
from src.routes import usuario

def create_app():
    app = Flask(__name__)
    
    # CORS permitido correctamente
    CORS(app, resources={r"*": {"origins": "*"}})

    # Cargar configuración
    #app.config.from_object(config['development'])
    app.config.from_object(config['production'])
    # Registrar rutas
    app.register_blueprint(usuario.main, url_prefix='/api/usuario')
    @app.route("/")
    def home():
        # *** AÑADE ESTA LÍNEA TEMPORALMENTE ***
        # Importa aquí para evitar errores de importación circular
        from src.database.db import get_connection 
        
        # Intenta obtener la conexión
        try:
            conn = get_connection()
            conn.close()
            return {"message": "API y DB funcionando correctamente"}, 200
        except Exception as ex:
            # Si falla, devuelve un 500 y el mensaje de error.
            return {"message": f"API funcionando, pero FALLÓ CONEXIÓN DB: {str(ex)}"}, 500
        
    # Errores
    @app.errorhandler(404)
    def page_not_found(error):
        return "<h1>Not found page</h1>", 404
    
    return app

# Flask CLI con local run
#app = create_app()

#if __name__ == "__main__":
 #   app.run()
