SECRETS = [
    # AWS
    'AWS_ACCESS_KEY_ID', 'AWS_SECRET_ACCESS_KEY',
    # Azure
    'AZURE_SUBSCRIPTION_ID', 'AZURE_TENANT_ID',
    'AZURE_CLIENT_ID', 'AZURE_CLIENT_SECRET',
    # Kong
    'KONG_EXPORTER_URL', 'KONG_EXPORTER_KEY'
]

def envVarToYaml(string):
    return string.lower().replace('_', '-')
def yamlVarToEnv(string):
    return string.upper().replace('-', '_')

def ensureDNS1123(name):
    return name \
            .lower() \
            .replace(' ', '-') \
            .replace('æ', 'ae') \
            .replace('ø', 'oe') \
            .replace('å', 'aa')

def extractSecrets(harvester):
    env = {
        'STACK': harvester['stack'],
        'STACK_NAME': harvester.get('name', 'default')
    }

    for secret in SECRETS:
        secret_as_yaml_var = envVarToYaml(secret).split('-', 1)[1]

        if secret_as_yaml_var in harvester:
            env[secret] = harvester[secret_as_yaml_var]

    return env

## Creator env handling
def extractSourceEnv(producer):
    return {
        'SOURCE_NAME': ensureDNS1123(producer['name']),
        'SOURCE_IDENTIFIER': producer['identifier']
    }

