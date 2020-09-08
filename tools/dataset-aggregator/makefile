PYTHON=.venv/bin/python
PIP=.venv/bin/pip

REPOSITORY=container-registry.oslo.kommune.no
NAME=dataset-harvest-aggregator
VERSION=0.0.3

.PHONY: help
help: ## Print this menu
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'

.env:
	@echo "AGGREGATIONS_PATH=" >> .env
	@echo "RESULT_PATH=" >> .env
	@echo "TMP_PATH=../../data/tmp" >> .env

.venv:
	python -m venv .venv
	.venv/bin/pip install -r requirements.txt

init: .env .venv ## Initialize environment

build-image: ## Build docker image
	docker build \
		--tag ${REPOSITORY}/${NAME}:latest \
		--tag ${REPOSITORY}/${NAME}:${VERSION} \
		.
push: build-image ## Push docker image
	docker push ${REPOSITORY}/${NAME}:latest
	docker push ${REPOSITORY}/${NAME}:${VERSION}

run-docker: ## Run locally with Docker
	@docker run \
		--rm \
		--env-file ./.env \
		${REPOSITORY}/${NAME}

.PHONY: /data
/data:
	mkdir -p ../../data/dataset/tmp
	mkdir -p ../../data/dataset/20_aggregations
	mkdir -p ../../data/dataset/30_result

run: /data ## Run locally
	export `cat .env` && cat ../../data/dataset/10_raw/dataplatform-datasets.json | ${PYTHON} aggregator.py

deploy: ## Deploy to Kubernetes
	kubectl apply -f aggregation_job.yaml

clean:
	rm -r .venv
