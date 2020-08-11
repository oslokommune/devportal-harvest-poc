import json
import os
import requests
import subprocess
from flask import Flask

app = Flask(__name__)

DATA_DIR = os.environ['PROVIDER_DATA_DIR']

@app.route('/apis', methods=['GET'])
def get_apis():
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
    return json.dumps(apis)
