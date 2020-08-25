PYTHON=.venv/bin/python
PIP=.venv/bin/pip

.venv:
	python -m venv .venv
	${PIP} install \
		-r requirements.txt \
		-r distributor/dataplatform/requirements.txt

.env:
	@echo "SOURCE_NAME=# Name of the API gateway owner" >> .env
	@echo "SOURCE_IDENTIFIER=#URL to the API gateway owner containing json information about them" >> .env
	@echo "# Dataplatform distributor" >> .env
	@echo "ORIGO_ENVIRONMENT=dev" >> .env
	@echo "ORIGO_USERNAME=# Byrbruker" >> .env
	@echo "ORIGO_PASSWORD=# Byrpassord" >> .env
	@echo "Remember to run 'export $$(cat .env)'"

init: .venv .env

../data/:
	mkdir -p ../data

latest.ttl: ../data/
	${PYTHON} ../tools/json_merger.py ../data/ | ${PYTHON} ../tools/latest_provider/scripts/turtle.py > latest.ttl

distribute: ../data/
	${PYTHON} ../tools/json_merger.py ../data/ | ${PYTHON} distributors/dataplatform/dataplatform.py

clean:
	rm -r .venv
	rm latest.ttl
