PYTHON=.venv/bin/python
PIP=.venv/bin/pip

init:
	python -m venv .venv
	${PIP} install -r requirements.txt

create-dotenv-file:
	@echo "# Dataplatform distributor" >> .env
	@echo "ORIGO_ENVIRONMENT=dev" >> .env
	@echo "ORIGO_USERNAME=# Byrbruker" >> .env
	@echo "ORIGO_PASSWORD=# Byrpassord" >> .env
	@echo "\n# AWS harvester" >> .env
	@echo "AWS_ACCESS_KEY_ID=# AWS iam user key id" >> .env
	@echo "AWS_SECRET_ACCESS_KEY=# AWS iam user access key" >> .env
	@echo "\n# Azure harvester" >> .env
	@echo "AZURE_CLIENT_ID=" >> .env
	@echo "AZURE_CLIENT_SECRET=" >> .env
	@echo "AZURE_SUBSCRIPTION_ID=" >> .env
	@echo "AZURE_TENANT_ID=" >> .env
	@echo "Remember to run 'export $$(cat .env)'"

harvest:
	mkdir -p data
	${PYTHON} harvester/aws.py >> data/aws.json

distribute:
	${PYTHON} distributor/dataplatform.py data/aws.json

turtle:
	@${PYTHON} tools/json_merger.py data | ${PYTHON} writer/turtle.py
