from flask import Flask
from flask_cors import CORS
from src.config import config
#routes
from src.routes import usuario

app=Flask(__name__)
CORS(app, resources={r"*": {"origins": "*"}})

def page_not_found(error):
    return "<h1>Not found page</h1>", 404

if __name__ == '__main__':
    app.config.from_object(config['development'])
    
    app.register_blueprint(usuario.main, url_prefix='/api/usuario')
    
    app.register_error_handler(404,page_not_found)
    app.run()