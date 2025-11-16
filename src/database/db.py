# src/database/db.py

import psycopg2
from psycopg2 import DatabaseError
from decouple import config
import sys # <-- Importar sys

def get_connection():
    print("Intentando conexión a PostgreSQL...") 
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
        # Usar sys.stderr.write para garantizar que el error sea visible
        sys.stderr.write("-" * 50 + "\n")
        sys.stderr.write("🚨 ERROR FATAL DE CONEXIÓN A POSTGRESQL 🚨\n")
        sys.stderr.write(f"Error: {ex}\n")
        sys.stderr.write("Verifica PGSQL_HOST, PGSQL_PORT y las credenciales.\n")
        sys.stderr.write("-" * 50 + "\n")
        
        # Esta línea levantará el error para que Flask/Gunicorn lo maneje
        raise ex