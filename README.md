# Flask Redis API con Tareas en Background

Este proyecto es una aplicación Flask organizada utilizando blueprints. Implementa:
- **API con Flask Blueprints:** Endpoint para consultar datos almacenados en una base de datos Redis.
- **Proceso en Background:** Al iniciar el servicio, se lanza un proceso que cada 5 minutos realiza peticiones HTTP a una lista de URLs (definidas en `urls.json`), recopilando el código de estado y un fragmento del mensaje, y almacenándolos en Redis.
- **Sistema de Caché:** Utilizando Flask-Caching para cachear respuestas de endpoints.
- **Documentación OpenAPI/Swagger:** Documentación interactiva accesible en `/apidocs/`.
- **Docker y Kubernetes:** Incluye un `Dockerfile` para empaquetar la aplicación, facilitando su despliegue en contenedores y en entornos Kubernetes.


## Requisitos

- Python 3.8 o superior.
- Una instancia de Redis.

## Instalación

1. **Clonar el repositorio:**
    ```bash
    git clone <URL_DEL_REPOSITORIO>
    cd flask-redis-api
    ```

2. **Instalar dependencias:**
    ```bash
    pip install -r requirements.txt
    ```

3. **Configurar Redis:**

   Por defecto, la aplicación se conecta a `redis:6379`. Si tu Redis se ejecuta en otro host o puerto, ajusta la configuración en `app/config.py` o mediante variables de entorno.

## Ejecución

Para iniciar la aplicación en modo desarrollo:
```bash
python run.py


La aplicación se ejecutará en http://0.0.0.0:5000.

Accede a la documentación interactiva en: http://0.0.0.0:5000/apidocs/
curl http://0.0.0.0:5000/api/status
