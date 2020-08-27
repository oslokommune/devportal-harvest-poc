REPOSITORY=container-registry.oslo.kommune.no
NAME=aws-harvester
VERSION=0.0.3

.venv:
	python -m venv .venv
	.venv/bin/pip install -r requirements.txt

.env:
	@echo "SOURCE_NAME=" >> .env
	@echo "SOURCE_IDENTIFIER=" >> .env
	@echo "AWS_ACCESS_KEY_ID=" >> .env
	@echo "AWS_SECRET_ACCESS_KEY=" >> .env
	@echo "AWS_REGION=" >> .env

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
		--env-file ./.env \
		${REPOSITORY}/${NAME}
