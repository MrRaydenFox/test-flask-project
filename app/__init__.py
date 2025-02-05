from flask import Flask
from flask_caching import Cache
from flasgger import Swagger
from .config import Config
import yaml
import redis

cache = Cache()

def create_app():
    # Crear la aplicación Flask
    app = Flask(__name__)
    app.config.from_object(Config)
    
    # Inicializar cache
    cache.init_app(app)
    
    # Conexión a Redis
    app.redis_client = redis.Redis(
        host=Config.REDIS_HOST,
        port=Config.REDIS_PORT,
        db=0,
        decode_responses=True
    )
    
    # Registrar blueprint de la API versión 1
    from app.api.v1.api import api_v1_bp
    app.register_blueprint(api_v1_bp, url_prefix='/api/v1')
    
    # Cargar documentación desde el fichero YAML externo
    with open('docs/swagger.yml', 'r') as f:
        swagger_template = yaml.safe_load(f)
    Swagger(app, template=swagger_template)
    
    # Iniciar el proceso en background
    from app.tasks.tasks import start_scheduler
    start_scheduler(app)
    
    return app
