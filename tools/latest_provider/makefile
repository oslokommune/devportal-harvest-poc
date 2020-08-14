REPOSITORY=container-registry.oslo.kommune.no
NAME=latest-provider
VERSION=0.0.5
CHART_DIR=charts/latest_provider

build-image:
	docker build \
		--tag ${REPOSITORY}/${NAME}:${VERSION} \
		--tag ${REPOSITORY}/${NAME}:latest \
		.

push:
	docker push ${REPOSITORY}/${NAME}:${VERSION}
	docker push ${REPOSITORY}/${NAME}:latest

run-docker:
	docker run --rm \
		--publish 5000:5000 \
		--env PROVIDER_DATA_DIR=/app/data \
		${REPOSITORY}/${NAME}:${VERSION}

#		--dry-run --debug
deploy-test:
	helm --tiller-namespace=developerportal-test --namespace=developerportal-test upgrade \
    --install ${NAME} ${CHART_DIR} \
    --reuse-values \
		--set version=${VERSION} \
    --values ${CHART_DIR}/values.yaml
