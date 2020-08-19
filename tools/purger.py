import subprocess
import sys

if len(sys.argv) != 2:
    print('Please specify type of jobs to purge. Type can be harvesters or distributors')
    sys.exit(1)
if sys.argv[1] not in ['harvesters', 'distributors']:
    print('The type must be either "harvesters" or "distributors"')
    sys.exit(1)

NAMESPACE = 'developerportal-test'

job_filter = ''
if sys.argv[1] == 'harvesters':
    job_filter = 'harvest'
elif sys.argv[1] == 'distributors':
    job_filter = 'distribute'

FETCH_JOBS_CMD = ['kubectl', f'--namespace={NAMESPACE}', 'get', 'cronjobs']
DELETE_JOBS_CMD = ['kubectl', f'--namespace={NAMESPACE}', 'delete']
FETCH_SECRETS_CMD = ['kubectl', f'--namespace={NAMESPACE}', 'get', 'secrets']
DELETE_SECRET_CMD = ['kubectl', f'--namespace={NAMESPACE}', 'delete']

fetch_jobs_process = subprocess.run(FETCH_JOBS_CMD, capture_output=True)
fetch_secrets_process = subprocess.run(FETCH_SECRETS_CMD, capture_output=True)

jobs = fetch_jobs_process.stdout.decode().split('\n')[1:]
secrets = fetch_secrets_process.stdout.decode()

commands = list()
for line in jobs:
    name = line.split(' ')[0]

    if job_filter in name:
        commands.append(DELETE_JOBS_CMD + [ 'cronjob.batch/' + name, ])

        if name in secrets:
            commands.append(DELETE_SECRET_CMD + ['secret/' + name, ])

print('The following commands will be run:\n')
for cmd in commands:
    print(' '.join(cmd))

answer = input('\nExecute? [y/N] ')

if answer.lower() != 'y':
    print('Canceled')
    sys.exit(0)

for cmd in commands:
    subprocess.run(cmd)
