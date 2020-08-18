REPOSITORY=container-registry.oslo.kommune.no
NAME=dataplatform-distributor
VERSION=0.0.2


build-image:
	docker build \
		--tag ${REPOSITORY}/${NAME}:${VERSION} \
		--tag ${REPOSITORY}/${NAME}:latest \
		.
push:
	docker push ${REPOSITORY}/${NAME}:${VERSION}
	docker push ${REPOSITORY}/${NAME}:latest

run:
	@docker run \
		--rm \
		--env-file ../../.env \
		${REPOSITORY}/${NAME}
