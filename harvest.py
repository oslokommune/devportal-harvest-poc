from subprocess import run
import sys
import yaml

from lib.env import extractSourceEnv, extractSecrets, extractMetadata
from lib.job import HarvestJob

data = yaml.load(sys.stdin.read(), Loader=yaml.FullLoader)

KUBECTL_APPLY = ['kubectl', '--namespace', 'developerportal-test', 'apply', '-f', '-']

if len(sys.argv) > 1:
    if '-d' in sys.argv:
        KUBECTL_APPLY.insert(1, '--dry-run=client')

def deploy(source, harvester):
    metadata_env = extractMetadata(harvester)
    stack_env = extractSecrets(harvester)
    source_env = extractSourceEnv(source)

    env = { **source_env, **stack_env, **metadata_env }
    template = HarvestJob.loadFile('charts/harvest_job.yaml', env)

    run(
        KUBECTL_APPLY,
        input = template.generateSecret().encode('utf-8')
    )

    run(
        KUBECTL_APPLY,
        input = str(template).encode('utf-8')
    )

for source in data['sources']:
    for harvester in source['harvesters']:
        deploy(source, harvester)
