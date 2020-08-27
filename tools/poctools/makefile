PYTHON=.venv/bin/python
PIP=.venv/bin/pip
TWINE=.venv/bin/twine

.venv:
	python -m venv .venv
	${PIP} install -r requirements.txt

/dist/: build
/build/: build

build: .venv
	${PYTHON} setup.py sdist bdist_wheel

publish: /dist/ /build/
	${TWINE} upload dist/*

clean:
	rm -r build/ || true
	rm -r dist/ || true
	rm -r origo_devportal_poctools.egg-info/ || true
	rm -r .venv || true
