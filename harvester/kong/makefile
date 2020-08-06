REPOSITORY=container-registry.oslo.kommune.no
NAME=kong-harvester


build:
	docker build --tag ${REPOSITORY}/${NAME} .

run:
	@docker run \
		--rm \
		--env-file ../../.env \
		${REPOSITORY}/${NAME}
