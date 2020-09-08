PYTHON=.venv/bin/python
PIP=.venv/bin/pip

REPOSITORY=container-registry.oslo.kommune.no
NAME=latest-provider
VERSION=0.0.11
CHART_DIR=charts/latest_provider

.PHONY: help
help: ## Print this menu
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'

init:
	python -m venv .venv
	${PIP} install -r requirements.txt

build-image: ## Builds docker image
	docker build \
		--tag ${REPOSITORY}/${NAME}:${VERSION} \
		--tag ${REPOSITORY}/${NAME}:latest \
		.

push: build-image ## Push docker image to docker registry
	docker push ${REPOSITORY}/${NAME}:${VERSION}
	docker push ${REPOSITORY}/${NAME}:latest

.PHONY: /data
/data:
	mkdir -p ../../data/dataservice
	mkdir -p ../../data/dataset

run-docker: /data build-image ## Run docker image
	docker run --rm \
		--name latest_provider \
		--publish 5000:5000 \
		--env PROVIDER_DATA_DIR=/app/data \
		--volume `pwd`/../../data:/app/data \
		${REPOSITORY}/${NAME}:${VERSION}

run-dataset-turtler:
	cat ../../data/dataset/30_result/public.json | ${PYTHON} scripts/dataset_turtler.py

#		--dry-run --debug
deploy-test: push ## Deploy to test
	helm --tiller-namespace=developerportal-test --namespace=developerportal-test upgrade \
    --install ${NAME} ${CHART_DIR} \
    --reset-values \
	--set version=${VERSION} \
    --values ${CHART_DIR}/values.yaml
