REPOSITORY=container-registry.oslo.kommune.no
NAME=latest-provider
CHART_DIR=charts/latest_provider

build-image:
	docker build \
		--tag ${REPOSITORY}/${NAME} \
		.

push:
	docker push ${REPOSITORY}/${NAME}:latest

#		--dry-run --debug
deploy-test:
	helm --tiller-namespace=developerportal-test --namespace=developerportal-test upgrade \
    --install ${NAME} ${CHART_DIR} \
    --reuse-values \
    --values ${CHART_DIR}/values.yaml
