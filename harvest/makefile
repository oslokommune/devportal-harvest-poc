PYTHON=.venv/bin/python
PIP=.venv/bin/pip

.venv:
	python -m venv .venv
	${PIP} install \
		-r requirements.txt \
		-r harvester/aws/requirements.txt \
		-r harvester/azure/requirements.txt \
		-r harvester/kong/requirements.txt

.env:
	@echo "# Required by all harvesters" >> .env
	@echo "SOURCE_NAME=# Name of the API gateway owner" >> .env
	@echo "SOURCE_IDENTIFIER=#URL to the API gateway owner containing json information about them" >> .env
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

init: .venv .env

../data/:
	mkdir -p ../data

harvest: ../data/
	${PYTHON} harvester/aws/aws.py > ../data/aws.json
	${PYTHON} harvester/azure/azure.py > ../data/azure.json
	${PYTHON} harvester/kong/kong.py > ../data/kong.json

clean:
	rm -r .venv
