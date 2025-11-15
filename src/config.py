from decouple import config
import os

class ProductionConfig:
    DEBUG = False
    DB_HOST = os.getenv("PGSQL_HOST")
    DB_USER = os.getenv("PGSQL_USER")
    DB_PASSWORD = os.getenv("PGSQL_PASSWORD")
    DB_DATABASE = os.getenv("PGSQL_DATABASE")
    DB_PORT = os.getenv("PGSQL_PORT")
class Config:
    SECRET_KEY = config('SECRET_KEY')

class DevelopmentConfig(Config):
    DEBUG = True

class ProductionConfig(Config):
    DEBUG = False

config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig
}
