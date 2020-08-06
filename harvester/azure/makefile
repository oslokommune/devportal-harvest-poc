REPOSITORY=container-registry.oslo.kommune.no
NAME=azure-harvester


build:
	docker build --tag ${REPOSITORY}/${NAME} .

run:
	@docker run \
		--rm \
		--env-file ../../.env \
		${REPOSITORY}/${NAME}
