import subprocess
import sys
import yaml

from origo.devportal.poctools.env import extractSourceEnv, extractSecrets, extractMetadata
from origo.devportal.poctools.job import HarvestJob

data = yaml.load(sys.stdin.read(), Loader=yaml.FullLoader)

KUBECTL_APPLY = ['kubectl', '--namespace', 'developerportal-test', 'apply', '-f', '-']

if len(sys.argv) > 1:
    if '-d' in sys.argv:
        KUBECTL_APPLY.insert(1, '--dry-run=server')


def deploy(source, harvester):
    metadata_env = extractMetadata(harvester)
    stack_env = extractSecrets(harvester)
    source_env = extractSourceEnv(source)

    env = {**source_env, **stack_env, **metadata_env}
    template = HarvestJob.loadFile('templates/harvest_job.yaml', env)

    subprocess.run(
        KUBECTL_APPLY,
        input=template.generateSecret().encode('utf-8')
    )

    subprocess.run(
        KUBECTL_APPLY,
        input=str(template).encode('utf-8')
    )


for source in data['sources']:
    for harvester in source['harvesters']:
        deploy(source, harvester)
