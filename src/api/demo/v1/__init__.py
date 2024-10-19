import requests
from flask import Blueprint, jsonify

from cache import cache

json_placeholder = "https://jsonplaceholder.typicode.com"

demo = Blueprint('demo_v1', __name__, template_folder='templates')

@demo.route('/comments', methods=['GET'])
def manage_secrets():
    """
    GET:    Consulta los secretos existente con el filtro indicado.
    """
    try:
        context = f'comments'
        response = call_json_placeholder(f'{context}')
        
        return response
    except Exception as ex:
        return jsonify({'error': { 'status': ex.status, 'code': ex.code, 'message': str(ex)}}), ex.status


def call_json_placeholder(context, method='GET', data=None):
    url = f'{json_placeholder}/{context}'
    
    response = requests.get(url)

    return response.json()
