import json
import time
import threading
import requests
from datetime import datetime

def fetch_urls(app):
    """Realiza peticiones a las URLs listadas en urls.json y almacena el resultado en Redis."""
    with app.app_context():
        redis_client = app.redis_client
        try:
            with open('urls.json', 'r') as f:
                urls = json.load(f)
        except Exception as e:
            app.logger.error(f"Error al cargar URLs: {e}")
            return

        for url in urls:
            try:
                response = requests.get(url)
                status_code = response.status_code
                # Se toma un fragmento del mensaje para no almacenar textos demasiado largos
                message = response.text[:100]
            except Exception as e:
                status_code = None
                message = str(e)

            # Construir el objeto a almacenar
            key = f"url_status:{url}"
            value = json.dumps({
                "timestamp": datetime.utcnow().isoformat(),
                "status_code": status_code,
                "message": message
            })
            redis_client.set(key, value)
            app.logger.info(f"Actualizado estado para {url}")

def scheduler(app):
    """Bucle infinito que ejecuta fetch_urls cada 5 minutos."""
    while True:
        fetch_urls(app)
        time.sleep(300)  # 5 minutos

def start_scheduler(app):
    """Inicia el proceso en background de forma no bloqueante."""
    thread = threading.Thread(target=scheduler, args=(app,), daemon=True)
    thread.start()
