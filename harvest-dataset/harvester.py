import requests
import os
import json
from origo.devportal.poctools.models import Dataset

DATASET_API_BASE_URL = os.environ['DATASET_API_BASE_URL']


def getDatasets():
    headers = {'accept': 'application/json'}
    response = requests.get(f"{DATASET_API_BASE_URL}/metadata/datasets", headers=headers)

    if response.status_code != 200:
        raise Exception(f"Got unexpected status code: {response.status_code}")

    return response.json()

# We only care about some fields in the dataset for now, we don't want to store everything.
def convertToOurDomainModel(datasets):
    result = []
    for dataset in datasets:
        stripped = Dataset()
        stripped.identifier = dataset['Id']
        stripped.title = dataset['title']
        stripped.description = dataset.get('description', '')
        stripped.publisher = dataset.get('publisher', '')

        result.append(stripped)

    return result

def toJSON(datasets):
    return json.dumps([dataset.serialize() for dataset in datasets])

try:
   input_datasets = getDatasets()
   output_datasets = convertToOurDomainModel(input_datasets)

   print(toJSON(output_datasets))
except Exception as ex:
   print("An error occurred when harvesting.")
   raise ex
