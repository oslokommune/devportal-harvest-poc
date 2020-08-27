import subprocess
import sys
import yaml

from origo.devportal.poctools.env import extractSecrets
from origo.devportal.poctools.job import DistributeJob

data = yaml.load(sys.stdin.read(), Loader=yaml.FullLoader)

KUBECTL_APPLY = ['kubectl', '--namespace', 'developerportal-test', 'apply', '-f', '-']

if len(sys.argv) > 1:
    if '-d' in sys.argv:
        KUBECTL_APPLY.insert(1, '--dry-run=client')


def deploy(distributor):
    env = extractSecrets(distributor)
    env['STACK'] = distributor['name']

    template = DistributeJob.loadFile('charts/distribute_job.yaml', env)

    subprocess.run(
        KUBECTL_APPLY,
        input=template.generateSecret().encode('utf-8')
    )

    subprocess.run(
        KUBECTL_APPLY,
        input=str(template).encode('utf-8')
    )


for distributor in data['distributors']:
    deploy(distributor)
