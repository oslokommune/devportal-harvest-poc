from subprocess import run
import sys
import yaml

from lib.env import extractSourceEnv, extractSecrets
from lib.job import Job

data = yaml.load(sys.stdin.read(), Loader=yaml.FullLoader)

KUBECTL_APPLY = ['kubectl', '--namespace', 'developerportal-test', 'apply', '-f', '-']

def deploy(source, harvester):
    stack_env = extractSecrets(harvester)
    source_env = extractSourceEnv(source)

    env = { **source_env, **stack_env }
    template = Job.loadFile('charts/job.yaml', env)

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
