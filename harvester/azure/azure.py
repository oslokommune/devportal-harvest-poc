#!/usr/bin/python
import json
import requests
import os
from build.lib.api import API
from build.lib.source import Source

CLIENT_ID = os.environ.get('AZURE_CLIENT_ID')
CLIENT_SECRET = os.environ.get('AZURE_CLIENT_SECRET')
SUBSCRIPTION_ID = os.environ.get('AZURE_SUBSCRIPTION_ID')
TENANT_ID = os.environ.get('AZURE_TENANT_ID')
RESOURCE_GROUP_NAME = os.environ.get('AZURE_RESOURCE_GROUP_NAME')
GATEWAY_NAME = os.environ.get('AZURE_GATEWAY_NAME')

def extractResourceGroupFromId(id_string):
    return id_string.split('/')[4]

def acquireToken(tenant_id, client_id, client_secret):
    url = f'https://login.microsoftonline.com/{tenant_id}/oauth2/token'
    data = {
        'grant_type': 'client_credentials',
        'client_id': client_id,
        'client_secret': client_secret,
        'resource': 'https://management.azure.com/'
    }
    headers = { 'Accept': 'application/json' }
    response = requests.post(url, data = data, headers = headers)

    return response.json()['access_token']

def getGateways(token, subscription_id):
    url = ''.join([
        'https://management.azure.com'
        f'/subscriptions/{subscription_id}',
        '/providers/Microsoft.ApiManagement',
        '/service?api-version=2019-12-01'
    ])

    headers = { 'Accept': 'application/json', 'Authorization': f'Bearer {token}' }

    response = requests.get(url, headers = headers)

    gateways = list()
    for gateway in response.json()['value']:
        gateways.append({
            'name': gateway['name'],
            'resourceGroup': extractResourceGroupFromId(gateway['id'])
        })

    return gateways

def getAPIs(token, subscription_id, gateway):
    url = ''.join([
        'https://management.azure.com',
        f'/subscriptions/{subscription_id}',
        f'/resourceGroups/{gateway["resourceGroup"]}',
        '/providers/Microsoft.ApiManagement',
        f'/service/{gateway["name"]}/apis?api-version=2019-12-01'
    ])

    headers = { 'Accept': 'application/json', 'Authorization': f'Bearer {token}' }

    response = requests.get(url, headers = headers)

    return response.json()['value']

token = acquireToken(TENANT_ID, CLIENT_ID, CLIENT_SECRET)
gateways = getGateways(token, SUBSCRIPTION_ID)

source = Source.loadFromEnv()
apis = list()
for gateway in gateways:
    apis += [ API(api['name'], source.identifier) for api in getAPIs(token, SUBSCRIPTION_ID, gateway) ]

print(json.dumps([ api.serialize() for api in apis ]))
