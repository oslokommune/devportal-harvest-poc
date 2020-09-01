import requests
import os
import json

DATASETS_BASE_URL = os.environ['DATASET_API_BASE_URL']


def get_datasets():
    headers = {'accept': 'application/json'}
    r = requests.get(f"{DATASETS_BASE_URL}/metadata/datasets", headers=headers)

    if r.status_code != 200:
        raise Exception(f"Got unexpected status code: {r.status_code}")

    return json.dumps(r.json())


try:
    datasets = get_datasets()
    print(datasets)
except Exception as ex:
    print("ERROR:")
    print(ex)
