REPOSITORY=container-registry.oslo.kommune.no
NAME=azure-harvester
VERSION=0.0.2

.venv:
	python -m venv .venv
	.venv/bin/pip install -r requirements.txt

build-image:
	docker build \
		--tag ${REPOSITORY}/${NAME}:latest \
		--tag ${REPOSITORY}/${NAME}:${VERSION} \
		.
push:
	docker push ${REPOSITORY}/${NAME}:latest
	docker push ${REPOSITORY}/${NAME}:${VERSION}

run:
	@docker run \
		--rm \
		--env-file ../../.env \
		${REPOSITORY}/${NAME}
