REPOSITORY=container-registry.oslo.kommune.no
NAME=kong-api-exporter

build:
	docker build \
		--tag ${REPOSITORY}/${NAME} \
		.

push:
	docker push ${REPOSITORY}/${NAME}
