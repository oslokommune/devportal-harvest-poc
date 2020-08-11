from subprocess import run
import sys
import yaml

from lib.env import extractStackEnv, extractCreatorEnv
from lib.job import Job

data = yaml.load(sys.stdin.read(), Loader=yaml.FullLoader)

KUBECTL_APPLY = ['kubectl', '--namespace', 'developerportal-test', 'apply', '-f', '-']

def deploy(creator, harvester):
    stack_env = extractStackEnv(harvester)
    creator_env = extractCreatorEnv(creator)

    env = { **creator_env, **stack_env }
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
