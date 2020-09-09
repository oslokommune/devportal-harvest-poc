PYTHON=.venv/bin/python
PIP=.venv/bin/pip

REPOSITORY=container-registry.oslo.kommune.no
NAME=dataplatform-dataset-harvester

.PHONY: help
help: ## Print this menu
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'

.venv:
	python -m venv .venv
	${PIP} install \
		-r harvester/requirements.txt

.env:
	@echo "DATASET_API_BASE_URL=https://api.data-dev.oslo.systems" >> .env

init: .venv .env ## Init environment

/data:
	mkdir -p ../data/dataset/10_raw

run: /data ## Run harvester
	export `cat .env` && ${PYTHON} harvester.py > ../data/dataset/10_raw/dataplatform-datasets.json
	cat ../data/dataset/10_raw/dataplatform-datasets.json

build:
	docker build \
		--tag ${REPOSITORY}/${NAME} \
		.

run-docker: ## Run harvester in a docker container
	docker run \
		--rm \
		--env-file ./.env \
		${REPOSITORY}/${NAME}

push: build
	docker push ${REPOSITORY}/${NAME}

deploy: push ## Deploy harvester to Kubernetes
	kubectl apply -f harvest_job.yaml

clean: ## Clean stuff
	rm -r .venv
