import json
import os
import requests
import subprocess
from flask import Flask, make_response, request, Response

app = Flask(__name__)

DATA_DIR = os.environ['PROVIDER_DATA_DIR']

def preflight():
    response = make_response()
    response.headers.add('Access-Control-Allow-Origin', '*')

    return response

@app.route('/apis', methods=['GET', 'OPTIONS'])
def get_apis():
    if request.method == 'OPTIONS':
        return preflight()

    apis = []

    cmd = ['python', 'json_merger.py', DATA_DIR]
    merger = subprocess.run(cmd, capture_output=True)
    data = json.loads(merger.stdout.decode())

    for item in data:
        api = {
            'title': item['title'],
            'publisher': item['publisher']
        }
        apis.append(api)

    # TODO: Implement paging
    response = make_response(json.dumps(apis))
    response.mimetype = 'application/json'
    response.headers['Access-Control-Allow-Origin'] = '*'

    return response
