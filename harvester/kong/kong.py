import json
import requests
import os
from build.lib.api import API
from build.lib.source import Source

URL = os.environ['KONG_EXPORTER_URL']
KEY = os.environ['KONG_EXPORTER_KEY']

response = requests.get(URL, headers={'apikey': KEY})

source = Source.loadFromEnv()
apis = [ API(api['title'], source.identifier) for api in response.json() ]

print(json.dumps([ api.serialize() for api in apis ]))
