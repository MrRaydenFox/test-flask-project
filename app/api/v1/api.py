import json
from flask import Blueprint, jsonify, current_app
from app import cache

api_v1_bp = Blueprint('api_v1', __name__)

@api_v1_bp.route('/status', methods=['GET'])
@cache.cached(timeout=60)  # Cachea la respuesta durante 60 segundos
def get_status():
    redis_client = current_app.redis_client
    keys = redis_client.keys('url_status:*')
    data = []
    for key in keys:
        url = key.split("url_status:")[1]
        value = redis_client.get(key)
        if value:
            record = json.loads(value)
            record['url'] = url
            data.append(record)
    return jsonify({"data": data})
