import os

class Config:
    # Configuración de la aplicación
    DEBUG = os.getenv('DEBUG', True)
    SECRET_KEY = os.getenv('SECRET_KEY', 'mysecretkey')

    # Configuración de Redis
    REDIS_HOST = os.getenv('REDIS_HOST', 'localhost')
    REDIS_PORT = int(os.getenv('REDIS_PORT', 6379))

    # Configuración del cache
    CACHE_TYPE = 'SimpleCache'
