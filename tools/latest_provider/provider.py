import json
import os
import subprocess
from flask import Flask, make_response, request, Response
from logging.config import dictConfig

DATA_DIR = os.environ['PROVIDER_DATA_DIR']
DATASERVICE_DIR = os.path.join(DATA_DIR, 'dataservice')
DATASET_DIR = os.path.join(DATA_DIR, 'dataset')

app = Flask(__name__)

# Configure logging
dictConfig({
    'version': 1,
    'root': {
        'level': 'INFO'
    }
})


def preflight():
    response = make_response()
    response.headers.add('Access-Control-Allow-Origin', '*')

    return response


def toJSONResponse(data):
    response = make_response(json.dumps(data))
    response.mimetype = 'application/json'

    return response


def apisToTurtleResponse(apis):
    cmd = ['python', 'scripts/turtle.py']
    process = subprocess.run(
        cmd,
        capture_output=True,
        input=json.dumps(apis).encode('utf-8')
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
    with open(os.path.join(DATASERVICE_DIR, '30_result', 'public.json'), 'r') as f:
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
        response = toJSONResponse(apis)
    elif 'text/turtle' in mimetypes:
        response = apisToTurtleResponse(apis)
    else:
        response = make_response(f'unknown mimetype {mimetypes}')

    response.headers['Access-Control-Allow-Origin'] = '*'

    return response


def datasetsToTurtleResponse(datasets):
    cmd = ['python', 'scripts/dataset_turtler.py']
    process = subprocess.run(
        cmd,
        capture_output=True,
        input=json.dumps(datasets).encode('utf-8')
    )

    if process.returncode != 0:
        app.logger.error("Process returned with non-zero exit code")
        app.logger.error(process.stdout.decode())
        app.logger.error(process.stderr.decode())
        process.check_returncode()

    response = make_response(process.stdout.decode())
    response.mimetype = 'text/turtle'

    return response


# Output shouldn't contain visibility for now.
def remove_visibility(datasets):
    for d in datasets:
        d.pop("visibility", None)


@app.route('/datasets', methods=['GET', 'OPTIONS'])
def get_datasets():
    if request.method == 'OPTIONS':
        return preflight()

    with open(os.path.join(DATASET_DIR, '30_result', 'public.json'), 'r') as f:
        datasets = json.loads(f.read())

    remove_visibility(datasets)

    mimetypes = request.headers['Accept'].split(',')

    if 'application/json' in mimetypes:
        response = toJSONResponse(datasets)
    elif 'text/turtle' in mimetypes:
        response = datasetsToTurtleResponse(datasets)
    else:
        response = make_response(f'unknown mimetype {mimetypes}')

    response.headers['Access-Control-Allow-Origin'] = '*'

    return response
