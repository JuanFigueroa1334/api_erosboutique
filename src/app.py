from flask import Flask
from flask_cors import CORS
from src.config import config
from src.routes import usuario

def create_app():
    app = Flask(__name__)
    
    # CORS permitido correctamente
    CORS(app, resources={r"*": {"origins": "*"}})

    # Cargar configuración
    app.config.from_object(config['development'])

    # Registrar rutas
    app.register_blueprint(usuario.main, url_prefix='/api/usuario')

    # Errores
    @app.errorhandler(404)
    def page_not_found(error):
        return "<h1>Not found page</h1>", 404
    
    return app

# Flask CLI con local run
app = create_app()

if __name__ == "__main__":
    app.run()
