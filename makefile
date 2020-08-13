PYTHON=.venv/bin/python
PIP=.venv/bin/pip

init:
	python -m venv .venv
	${PIP} install -r requirements.txt

# This is only relevant for running the scripts locally
create-dotenv-file:
	@echo "SOURCE_NAME=# Name of the API gateway owner" >> .env
	@echo "SOURCE_IDENTIFIER=#URL to the API gateway owner containing json information about them" >> .env
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
	@echo "\n# Kong harvester" >> .env
	@echo "KONG_EXPORTER_URL=" >> .env
	@echo "KONG_EXPORTER_KEY=" >> .env
	@echo "Remember to run 'export $$(cat .env)'"

build:
	mkdir -p harvester/aws/build
	mkdir -p harvester/azure/build
	mkdir -p harvester/kong/build
	cp -r harvester/lib harvester/aws/build/lib
	cp -r harvester/lib harvester/azure/build/lib
	cp -r harvester/lib harvester/kong/build/lib
clean:
	rm -r harvester/aws/build
	rm -r harvester/azure/build
	rm -r harvester/kong/build

/data/:
	mkdir -p data

harvest: /data/
	${PYTHON} harvester/aws/aws.py > data/aws.json
	${PYTHON} harvester/azure/azure.py > data/azure.json
	${PYTHON} harvester/kong/kong.py > data/kong.json

turtle:
	@${PYTHON} tools/json_merger.py data | ${PYTHON} writer/turtle.py
