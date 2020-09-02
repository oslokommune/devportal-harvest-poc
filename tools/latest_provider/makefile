PYTHON=.venv/bin/python
PIP=.venv/bin/pip

REPOSITORY=container-registry.oslo.kommune.no
NAME=latest-provider
VERSION=0.0.9
CHART_DIR=charts/latest_provider

.PHONY: help
help: ## Print this menu
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'

init:
	python -m venv .venv
	${PIP} install -r requirements.txt

build-image:
	docker build \
		--tag ${REPOSITORY}/${NAME}:${VERSION} \
		--tag ${REPOSITORY}/${NAME}:latest \
		.

push: build-image ## Push docker image to docker registry
	docker push ${REPOSITORY}/${NAME}:${VERSION}
	docker push ${REPOSITORY}/${NAME}:latest

/data:
	mkdir -p ../../data/dataservice
	mkdir -p ../../data/dataset

run-docker: /data ## Run docker image
	docker run --rm \
		--name latest_provider \
		--publish 5000:5000 \
		--env PROVIDER_DATA_DIR=/app/data \
		--volume `pwd`/../../data:/app/data \
		${REPOSITORY}/${NAME}:${VERSION}

#		--dry-run --debug
deploy-test: push ## Deploy to test
	helm --tiller-namespace=developerportal-test --namespace=developerportal-test upgrade \
    --install ${NAME} ${CHART_DIR} \
    --reset-values \
	--set version=${VERSION} \
    --values ${CHART_DIR}/values.yaml
