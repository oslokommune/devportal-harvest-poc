import json
import os
import sys

from origo.devportal.poctools.models import API

DESCRIPTION_PATH = 'aggregation/description.json'
NAME_PATH = 'aggregation/name.json'
SPEC_URL_PATH = 'aggregation/specURL.json'
WHITELIST_PATH = 'aggregation/whitelist.json'

descriptionMap = dict()
if os.path.isfile(DESCRIPTION_PATH):
    with open(DESCRIPTION_PATH, 'r') as f:
        descriptionMap = json.loads(f.read())

nameMap = dict()
if os.path.isfile(NAME_PATH):
    with open(NAME_PATH, 'r') as f:
        nameMap = json.loads(f.read())

specURLMap = dict()
if os.path.isfile(SPEC_URL_PATH):
    with open(SPEC_URL_PATH, 'r') as f:
        specURLMap = json.loads(f.read())

whitelistMap = dict()
if os.path.isfile(WHITELIST_PATH):
    with open(WHITELIST_PATH, 'r') as f:
        whitelistMap = json.loads(f.read())

data = json.loads(sys.stdin.read())

aggregatedData = list()

for api in data:
    title = api['title']
    if whitelistMap.get(title, False) != False:
        aggregatedAPI = API(title, api['publisher'])

        aggregatedAPI.title = nameMap.get(title, title)
        aggregatedAPI.description = descriptionMap.get(title, '')
        aggregatedAPI.specificationURL = specURLMap.get(title, '')

        aggregatedData.append(aggregatedAPI.serialize())

print(json.dumps(aggregatedData))
