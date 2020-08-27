import json
import os

import boto3
from botocore.config import Config

from origo.devportal.poctools.models import API, Source

config = Config(
    region_name=os.environ['AWS_REGION'],
    signature_version='v4',
    retries={
        'max_attempts': 10,
        'mode': 'standard'
    }
)

credentials = {
    'aws_access_key_id': os.environ['AWS_ACCESS_KEY_ID'],
    'aws_secret_access_key': os.environ['AWS_SECRET_ACCESS_KEY']
}

source = Source.loadFromEnv()

clientv1 = boto3.client('apigateway', **credentials, config=config)
clientv2 = boto3.client('apigatewayv2', **credentials, config=config)

response_v1 = clientv1.get_rest_apis()
response_v2 = clientv2.get_apis()

apis = list()
for raw_api in response_v1['items']:
    api = API(raw_api['name'], source.identifier)

    apis.append(api.serialize())

for raw_api in response_v2['Items']:
    api = API(raw_api['Name'], source.identifier)

    apis.append(api.serialize())

print(json.dumps(apis))
