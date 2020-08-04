import json
import os
import requests
from flask import Flask

app = Flask(__name__)

KONG_ADMIN_URL = os.environ.get('KONG_ADMIN_URL', 'http://127.0.0.1:8001')

@app.route('/services', methods=['GET'])
def get_services():
    apis = []
    response = requests.get(f'{KONG_ADMIN_URL}/services')

    for item in response.json()['data']:
        api = {
            'title': item['name']
        }
        apis.append(api)

    # TODO: Implement paging
    return json.dumps(apis)
