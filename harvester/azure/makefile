REPOSITORY=container-registry.oslo.kommune.no
NAME=azure-harvester


build-image:
	docker build --tag ${REPOSITORY}/${NAME} .
push:
	docker push ${REPOSITORY}/${NAME}

run:
	@docker run \
		--rm \
		--env-file ../../.env \
		${REPOSITORY}/${NAME}
