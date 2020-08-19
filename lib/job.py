from subprocess import run
import base64
import yaml

from lib.env import SECRETS, envVarToYaml

def encodeString(raw):
    return base64.b64encode(raw.encode('utf-8')).decode()

class Job(object):
    @classmethod
    def loadFile(cls, path, env):
        jobTemplate = ''
        with open(path, 'r') as f:
            jobTemplate = f.read()

        interpolatedTemplate = run(
            ['envsubst'],
            capture_output = True,
            env = env,
            input = jobTemplate.encode('utf-8')
        )

        return cls(interpolatedTemplate.stdout.decode(), env)

    def __init__(self, template, env):
        self.template = yaml.load(template, Loader=yaml.FullLoader)
        self.env = env
        self.required_environment_vars = list()

    @property
    def name(self):
        return 'jobname'

    def __str__(self):
        env = list()

        for item in self.required_environment_vars:
            env.append({
                'name': item,
                'value': self.env[item]
            })

        for item in SECRETS:
            if item in self.env:
                env.append({
                    'name': item,
                    'valueFrom': {
                        'secretKeyRef': { 'name': f'{self.name}', 'key': envVarToYaml(item) }
                    }
                })

        computedTemplate = { **self.template }
        computedTemplate['metadata']['name'] = self.name
        computedTemplate['spec']['jobTemplate']['spec']['template']['spec']['containers'][0]['env'] = env

        return yaml.dump(computedTemplate)

    def generateSecret(self):
        secret = {
            'apiVersion': 'v1',
            'kind': 'Secret',
            'metadata': { 'name': self.name },
            'type': 'Opaque',
            'data': dict()
        }

        for item in SECRETS:
            if item in self.env:
                secret['data'][envVarToYaml(item)] = encodeString(self.env[item])

        return yaml.dump(secret)

class HarvestJob(Job):
    def __init__(self, template, env):
        super().__init__(template, env)
        self.required_environment_vars = [ 'SOURCE_NAME', 'SOURCE_IDENTIFIER' ]

    @property
    def name(self):
        return '-'.join([
            'harvest',
            self.env['SOURCE_NAME'],
            self.env['STACK'],
            self.env['STACK_NAME']
        ])


class DistributeJob(Job):
    def __init__(self, template, env):
        super().__init__(template, env)

    @property
    def name(self):
        return '-'.join([
            'distribute',
            self.env['STACK']
        ])
