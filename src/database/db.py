# src/database/db.py

import psycopg2
from psycopg2 import DatabaseError
from decouple import config
import logging # <-- Importar el módulo de logging

# Configurar un logger (opcional, pero buena práctica)
# Aunque Gunicorn ya configura un logger básico para stdout/stderr
# usarlo explícitamente es mejor.
# logging.basicConfig(level=logging.INFO) 
# logger = logging.getLogger(__name__)

def get_connection():
    # logger.info("Intentando conexión a PostgreSQL...")
    print("Intentando conexión a PostgreSQL...") # Dejar el print para un feedback rápido
    try:
        connection = psycopg2.connect(
            host=config('PGSQL_HOST'),
            user=config('PGSQL_USER'),
            password=config('PGSQL_PASSWORD'),
            database=config('PGSQL_DATABASE'),
            port=config('PGSQL_PORT')
        )
        print("Conexión a PostgreSQL exitosa.")
        return connection
        
    except DatabaseError as ex:
        # Usar logging.error o simplemente print() la información de la excepción
        # Al usar print() o stderr, Railway capturará el output.
        print("-" * 50)
        print("🚨 ERROR FATAL DE CONEXIÓN A POSTGRESQL 🚨")
        print(f"Error: {ex}")
        print("Verifica PGSQL_HOST, PGSQL_PORT y las credenciales.")
        print("-" * 50)
        
        # Opcionalmente, puedes usar:
        # logging.error("Error al conectar con PostgreSQL:", exc_info=True)
        
        # Esta línea es CLAVE: asegura que la traza completa se propague
        raise ex