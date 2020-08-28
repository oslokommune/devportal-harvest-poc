REPOSITORY=container-registry.oslo.kommune.no
NAME=harvest-aggregator
VERSION=0.0.1

.env:
	@echo "AGGREGATIONS_PATH=" >> .env
	@echo "RESULT_PATH=" >> .env

.venv:
	python -m venv .venv
	.venv/bin/pip install -r requirements.txt

init: .env .venv

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

clean:
	rm -r .venv
