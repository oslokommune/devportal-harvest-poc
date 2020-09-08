PYTHON=.venv/bin/python
PIP=.venv/bin/pip
TWINE=.venv/bin/twine

get-gopass-secret = $(or $(shell gopass show $(2) devportal/$(1)), $(error gopass command failed))

help: ## print this menu
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'

.venv:
	python -m venv .venv
	${PIP} install -r requirements.txt

init: .venv ## Initialize project

build: .venv ## Build distribution files
	${PYTHON} setup.py sdist bdist_wheel

/dist/: build
/build/: build
publish: clean /dist/ /build/ ## Publish to PyPi
	$(eval PYPI_TOKEN := $(call get-gopass-secret,poc/pypi-poctools-token,-o))
	@${TWINE} upload --non-interactive --username __token__ --password ${PYPI_TOKEN} dist/*

clean: ## Clean out the build files
	rm -r build/ || true
	rm -r dist/ || true
	rm -r origo_devportal_poctools.egg-info/ || true

purge: clean ## Clean out all generated files
	rm -r .venv || true

test: ## Run the library's tests.
	${PYTHON} -m tests.dataset_test
