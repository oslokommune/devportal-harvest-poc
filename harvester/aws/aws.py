import json
import os

import boto3
from botocore.config import Config

from build.lib.source import Source
from build.lib.api import API

config = Config(
    region_name = 'eu-north-1',
    signature_version = 'v4',
    retries = {
        'max_attempts': 10,
        'mode': 'standard'
    }
)

credentials = {
    'aws_access_key_id': os.environ['AWS_ACCESS_KEY_ID'],
    'aws_secret_access_key': os.environ['AWS_SECRET_ACCESS_KEY']
}

source = Source.loadFromEnv()

client = boto3.client('apigateway', **credentials, config=config)
response = client.get_rest_apis()

apis = list()
for raw_api in response['items']:
    api = API(raw_api['name'], source.identifier)

    apis.append(api.serialize())

print(json.dumps(apis))
