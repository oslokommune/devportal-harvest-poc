def ensureDNS1123(name):
    return name \
        .lower() \
        .replace(' ', '-') \
        .replace('æ', 'ae') \
        .replace('ø', 'oe') \
        .replace('å', 'aa')

## Stack env handling
def extractAWSEnv(harvester):
    env = dict()

    env['AWS_ACCESS_KEY_ID'] = harvester['access_key_id']
    env['AWS_SECRET_ACCESS_KEY'] = harvester['secret_access_key']

    return env
def extractAzureEnv(harvester):
    env = dict()

    env['AZURE_CLIENT_ID'] = harvester['client_id']
    env['AZURE_CLIENT_SECRET'] = harvester['client_secret']
    env['AZURE_SUBSCRIPTION_ID'] = harvester['subscription_id']
    env['AZURE_TENANT_ID'] = harvester['tenant_id']

    return env
def extractKongEnv(harvester):
    env = dict()

    env['KONG_EXPORTER_URL'] = harvester['exporter_url']
    env['KONG_EXPORTER_KEY'] = harvester['exporter_key']

    return env

def extractStackEnv(harvester):
    env = dict()

    if harvester['stack'] == 'aws':
        env = extractAWSEnv(harvester)
    elif harvester['stack'] == 'azure':
        env = extractAzureEnv(harvester)
    elif harvester['stack'] == 'kong':
        env = extractKongEnv(harvester)

    return { 'STACK': harvester['stack'], **env }

## Creator env handling
def extractCreatorEnv(producer):
    return {
        'SOURCE_NAME': ensureDNS1123(producer['name']),
        'SOURCE_IDENTIFIER': producer['identifier']
    }
