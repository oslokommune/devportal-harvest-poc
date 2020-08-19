from subprocess import run
import sys
import yaml

from lib.env import extractSourceEnv, extractSecrets
from lib.job import DistributeJob

data = yaml.load(sys.stdin.read(), Loader=yaml.FullLoader)

KUBECTL_APPLY = ['kubectl', '--namespace', 'developerportal-test', 'apply', '-f', '-']

def deploy(distributor):
    env = extractSecrets(distributor)
    env['STACK'] = distributor['name']

    template = DistributeJob.loadFile('charts/distribute_job.yaml', env)

    run(
        KUBECTL_APPLY,
        input = template.generateSecret().encode('utf-8')
    )

    run(
        KUBECTL_APPLY,
        input = str(template).encode('utf-8')
    )

for distributor in data['distributors']:
    deploy(distributor)
