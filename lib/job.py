from subprocess import run
import base64
import yaml

SECRETS = [
    # AWS
    'AWS_ACCESS_KEY_ID', 'AWS_SECRET_ACCESS_KEY',
    # Azure
    'AZURE_SUBSCRIPTION_ID', 'AZURE_TENANT_ID',
    'AZURE_CLIENT_ID', 'AZURE_CLIENT_SECRET',
    # Kong
    'KONG_EXPORTER_URL', 'KONG_EXPORTER_KEY'
]

def encodeString(raw):
    return base64.b64encode(raw.encode('utf-8')).decode()

def envVarToYaml(string):
    return string.lower().replace('_', '-')

class Job():
    @staticmethod
    def loadFile(path, env):
        jobTemplate = ''
        with open(path, 'r') as f:
            jobTemplate = f.read()

        interpolatedTemplate = run(
            ['envsubst'],
            capture_output = True,
            env = env,
            input = jobTemplate.encode('utf-8')
        )

        return Job(interpolatedTemplate.stdout.decode(), env)

    def __init__(self, template, env):
        self.template = yaml.load(template, Loader=yaml.FullLoader)
        self.env = env

    def __str__(self):
        env = list()

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

    @property
    def name(self):
        return '-'.join([
            'harvest',
            self.env['CREATOR_NAME'],
            self.env['STACK']
        ])

    def generateSecret(self):
        secret = {
            'apiVersion': 'v1',
            'kind': 'Secret',
            'metadata': { 'name': self.name },
            'type': 'Opaque',
        }

        data = dict()

        for item in SECRETS:
            if item in self.env:
                data[envVarToYaml(item)] = encodeString(self.env[item])

        secret['data'] = data

        return yaml.dump(secret)
