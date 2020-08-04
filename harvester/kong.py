import json
import requests
import os

URL = os.environ['KONG_EXPORTER_URL']
KEY = os.environ['KONG_EXPORTER_KEY']

response = requests.get(URL, headers={'apikey': KEY})

print(json.dumps(response.json()))
