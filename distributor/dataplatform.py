import datetime
import subprocess
import sys
from origo.data.upload import Upload
from origo.data.dataset import Dataset
from origo.config import Config

origo_config = Config(env='dev')

data_uploader = Upload(config=origo_config)
dataset = Dataset(config=origo_config)

dataset_id = 'api-listen'
filename = sys.argv[1]

edition_data = {
    'edition': datetime.datetime.utcnow().replace(tzinfo = datetime.timezone.utc).isoformat(),
    'description': 'Update',
    'startTime': '2020-01-01',
    'endTime': '2020-12-31'
}

version = '1'
edition = dataset.create_edition(dataset_id, version, data = edition_data)
editionId = edition['Id'].rsplit('/', 1)[1]

try:
    status = data_uploader.upload(filename, dataset_id, version, editionId)
except Exception as e:
    sys.exit(1)
