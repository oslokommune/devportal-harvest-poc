import datetime
import os
import subprocess
import sys
from origo.data.upload import Upload
from origo.data.dataset import Dataset
from origo.config import Config

DATASET_ID = os.environ['DATAPLATFORM_DATASET_ID']

TMP_PATH = '/tmp/api_export.json'

origo_config = Config(env='dev')

data_uploader = Upload(config=origo_config)
dataset = Dataset(config=origo_config)

with open(TMP_PATH, 'w') as f:
    f.write(sys.stdin.read())

edition_data = {
    'edition': datetime.datetime.utcnow().replace(tzinfo = datetime.timezone.utc).isoformat(),
    'description': 'Update',
    'startTime': '2020-01-01',
    'endTime': '2020-12-31'
}

version = '1'
edition = dataset.create_edition(DATASET_ID, version, data = edition_data)
editionId = edition['Id'].rsplit('/', 1)[1]

try:
    status = data_uploader.upload(TMP_PATH, DATASET_ID, version, editionId)
except Exception as e:
    sys.exit(1)
