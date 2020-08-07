from subprocess import run, PIPE
import sys
import yaml

from lib.env import extractStackEnv, extractCreatorEnv

data = yaml.load(sys.stdin.read(), Loader=yaml.FullLoader)

jobTemplate = ''
with open('charts/job.yaml') as f:
    jobTemplate = f.read()

def deploy(creator, harvester):
    stack_env = extractStackEnv(harvester)
    creator_env = extractCreatorEnv(creator)

    env = { **creator_env, **stack_env }

    interpolatedTemplate = run(
        ['envsubst'],
        capture_output=True,
        env=env,
        input=jobTemplate.encode('utf-8')
    )

    deployment = run(
        ['kubectl', '--namespace', 'developerportal-test', 'apply', '-f', '-'],
        capture_output=True,
        input=interpolatedTemplate.stdout
    )

    print(deployment.stdout.decode())

for creator in data['creators'][:1]:
    for harvester in creator['harvesters']:
        deploy(creator, harvester)
