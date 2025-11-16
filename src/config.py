# src/config.py

import os # ⬅️ Importar el módulo os
# from decouple import config # ⬅️ Comentar o eliminar esta línea
from decouple import config # Mantenemos la importación si la necesitas para otras variables, pero usaremos os.environ

class Config:
    # Usar os.environ para leer la variable. Si no existe, usa un valor de respaldo temporal.
    # Esto garantiza que el worker no falle si la variable no se sincroniza correctamente en Railway.
    SECRET_KEY = os.environ.get('SECRET_KEY', 'default_fallback_secret_key_12345')

class DevelopmentConfig(Config):
    DEBUG = True

class ProductionConfig(Config):
    DEBUG = False

config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig
}