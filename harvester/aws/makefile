REPOSITORY=container-registry.oslo.kommune.no
NAME=aws-harvester


build:
	docker build --tag ${REPOSITORY}/${NAME} .

run:
	@docker run \
		--rm \
		--env-file ../../.env \
		${REPOSITORY}/${NAME}
