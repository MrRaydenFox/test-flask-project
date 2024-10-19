import ipaddress
import json

import requests
from flask import Flask, abort, jsonify, request

from api.demo.v1 import demo as demo_v1
from api.demo.v2 import demo as demo_v2
from cache import cache

app = Flask(__name__)
cache.init_app(app)

app.register_blueprint(demo_v1, url_prefix='/api/demo/v1')
app.register_blueprint(demo_v2, url_prefix='/api/demo/v2')


@app.route('/status', methods=['GET'])
def check():
    return jsonify({"status": "OK"})


# @app.before_request
# def limit_remote_addr():
#     ip_address = ipaddress.ip_address(request.remote_addr)
#     ip_network = ipaddress.ip_network('1.2.0.0/16')
#     list_addresses = ['127.0.0.1']

#     if request.remote_addr not in list_addresses and ip_address not in ip_network:
#         app.logger.info('Denegada la petición realizada por la ip ' + request.remote_addr + ' al no encontrarse en la lista de ips permitidas')
#         abort(403, "La petición realizada no ha sido adminitada. El acceso al servicio está restringido a personal autorizado")


if __name__ == '__main__':
    app.run(debug=True)
