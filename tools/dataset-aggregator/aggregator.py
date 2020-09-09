import json
import os
import sys
from shutil import move
from origo.devportal.poctools.models import Dataset
from origo.devportal.poctools.models import Visibility

AGGREGATIONS_PATH = os.environ['AGGREGATIONS_PATH']
RESULT_PATH = os.environ['RESULT_PATH']
TMP_PATH = os.environ['TMP_PATH']

VISIBILITY_PATH = os.path.join(AGGREGATIONS_PATH, 'visibility.json')

def aggregate(datasets, visibility_map=dict):
    aggregated_datasets = list()

    for dataset in datasets:
        aggregated = Dataset()
        aggregated.identifier = dataset["identifier"]
        aggregated.title = dataset["title"]
        aggregated.description = dataset.get("description", "")
        aggregated.publisher = dataset.get("publisher", "")
        aggregated.visibility = visibility_map.get(aggregated.identifier, Visibility.PRIVATE.value)

        aggregated_datasets.append(aggregated)

    return aggregated_datasets


def divideByVisibility(data):
    result = { level: list() for level in Visibility }

    for item in data:
        result[Visibility(item.visibility)].append(item.serialize())

    return result


def saveDataAsJSON(data, target_filename):
    temp_filename = os.path.join(TMP_PATH, target_filename + ".tmp")
    with open(temp_filename, 'w') as tmp_file:
        tmp_file.write(json.dumps(data))

    target_filename_path = os.path.join(RESULT_PATH, target_filename)

    move(temp_filename, target_filename_path)


visibilityMap = dict()
if os.path.isfile(VISIBILITY_PATH):
    with open(VISIBILITY_PATH, 'r') as f:
        visibilityMap = json.loads(f.read())

datasets = json.loads(sys.stdin.read())

aggregatedData = aggregate(datasets, visibilityMap)

dividedData = divideByVisibility(aggregatedData)

saveDataAsJSON(dividedData[Visibility.PUBLIC], 'public.json')
saveDataAsJSON(dividedData[Visibility.PROTECTED], 'protected.json')
