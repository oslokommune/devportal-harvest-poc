import json
import os
import requests
import subprocess
from flask import Flask, make_response, request, Response

app = Flask(__name__)

DATA_DIR = os.environ['PROVIDER_DATA_DIR']
DATASERVICE_DIR = os.path.join(DATA_DIR, 'dataservice')

def preflight():
    response = make_response()
    response.headers.add('Access-Control-Allow-Origin', '*')

    return response

def apisToJSONResponse(apis):
    response = make_response(json.dumps(apis))
    response.mimetype = 'application/json'

    return response
def apisToTurtleResponse(apis):
    cmd = ['python', 'scripts/turtle.py']
    process = subprocess.run(
        cmd,
        capture_output = True,
        input = json.dumps(apis).encode('utf-8')
    )

    response = make_response(process.stdout.decode())
    response.mimetype = 'text/turtle'

    return response

@app.route('/apis', methods=['GET', 'OPTIONS'])
def get_apis():
    if request.method == 'OPTIONS':
        return preflight()

    apis = []

    data = list()
    with open(os.path.join(DATASERVICE_DIR, '10_result', 'public.json'), 'r') as f:
        data = json.loads(f.read())

    for item in data:
        api = {
            'title': item['title'],
            'publisher': item['publisher']
        }
        apis.append(api)

    # TODO: Implement paging
    response = None
    mimetypes = request.headers['Accept'].split(',')

    if 'application/json' in mimetypes:
        response = apisToJSONResponse(apis)
    elif 'text/turtle' in mimetypes:
        response = apisToTurtleResponse(apis)
    else:
        response = make_response(f'unknown mimetype {mimetypes}')

    response.headers['Access-Control-Allow-Origin'] = '*'

    return response
