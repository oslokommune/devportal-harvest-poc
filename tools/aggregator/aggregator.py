import json
import os
import sys
from shutil import move

from origo.devportal.poctools.models import API, Visibility

AGGREGATIONS_PATH = os.environ['AGGREGATIONS_PATH']
RESULT_PATH = os.environ['RESULT_PATH']

DESCRIPTION_PATH = os.path.join(AGGREGATIONS_PATH, 'description.json')
NAME_PATH = os.path.join(AGGREGATIONS_PATH, 'name.json')
SPEC_URL_PATH = os.path.join(AGGREGATIONS_PATH, 'specificationURL.json')
VISIBILITY_PATH = os.path.join(AGGREGATIONS_PATH, 'visibility.json')

def aggregate(raw_data, descriptionMap=dict(), nameMap=dict(),
        specificationURLMap=dict(), visibilityMap=dict):
    result = list()

    for api in data:
        aggregatedAPI = API(api['title'], api['publisher'])
        aggregatedAPI.id = api['title']

        aggregatedAPI.title = nameMap.get(aggregatedAPI.id, api['title'])
        aggregatedAPI.description = descriptionMap.get(aggregatedAPI.id, None)
        aggregatedAPI.specificationURL = specificationURLMap.get(aggregatedAPI.id, None)
        aggregatedAPI.visibility = visibilityMap.get(aggregatedAPI.id, Visibility.PRIVATE.value)

        result.append(aggregatedAPI)

    return result

def divideByVisibility(data):
    result = { level: list() for level in Visibility }

    for item in data:
        result[Visibility(item.visibility)] = item.serialize()

    return result

def saveDataAsJSON(data, file_name):
    TMP_PATH = os.path.join('/tmp', 'wip.json')

    with open(TMP_PATH, 'w') as f:
        f.write(json.dumps(data))

    move(TMP_PATH, os.path.join(RESULT_PATH, file_name))


descriptionMap = dict()
if os.path.isfile(DESCRIPTION_PATH):
    with open(DESCRIPTION_PATH, 'r') as f:
        descriptionMap = json.loads(f.read())

nameMap = dict()
if os.path.isfile(NAME_PATH):
    with open(NAME_PATH, 'r') as f:
        nameMap = json.loads(f.read())

specificationURLMap = dict()
if os.path.isfile(SPEC_URL_PATH):
    with open(SPEC_URL_PATH, 'r') as f:
        specificationURLMap = json.loads(f.read())

visibilityMap = dict()
if os.path.isfile(VISIBILITY_PATH):
    with open(VISIBILITY_PATH, 'r') as f:
        visibilityMap = json.loads(f.read())

data = json.loads(sys.stdin.read())

aggregatedData = aggregate(data, **{
    'descriptionMap': descriptionMap,
    'nameMap': nameMap,
    'specificationURLMap': specificationURLMap,
    'visibilityMap': visibilityMap
})

dividedData = divideByVisibility(aggregatedData)

saveDataAsJSON(dividedData[Visibility.PUBLIC], 'public.json')
saveDataAsJSON(dividedData[Visibility.PROTECTED], 'protected.json')
