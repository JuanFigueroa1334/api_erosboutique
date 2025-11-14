import psycopg2
from psycopg2 import DatabaseError
from decouple import config

def get_connection():
    print("Intentando conexión a PostgreSQL...")
    try:
        return psycopg2.connect(
            host=config('PGSQL_HOST'),
            user=config('PGSQL_USER'),
            password=config('PGSQL_PASSWORD'),
            database=config('PGSQL_DATABASE'),
            port=config('PGSQL_PORT', default=5432)
        )
    except DatabaseError as ex:
        print("Error al conectar con PostgreSQL:", ex)
        raise ex