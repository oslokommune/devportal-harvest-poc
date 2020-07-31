import json
import os

import boto3
from botocore.config import Config

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

client = boto3.client('apigateway', **credentials, config=config)


response = client.get_rest_apis()
apis = [ { 'name': item['name'] } for item in response['items'] ]

print(json.dumps(apis))
