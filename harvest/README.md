# Harvester

## Technical

### Production

#### Setup
1. `git clone git@github.com:oslokommune/devportal-harvest-poc.git`
2. `kubectl apply -f charts/harvest-output-pvc.yaml` This is the PVC where all
	 the harvesters will pipe their output to.
3. Create and configure a [sources.yaml](https://github.com/oslokommune/devportal-harvest-poc/blob/master/harvest/templates/sources_template.yaml) file

#### Deploy harvest jobs
1. Ensure the harvesters your sources require are available as Docker images.
	 See [Deploy harvester docker image](#Deploy harvester Docker image)
2. `cat sources.yaml | python harvest.py`

#### Deploy harvester Docker image
1. `cd harvest/harvester/<actual harvester>`
2. `make build-image`
3. `make push`

#### Local
1. `cd harvest/harvester/<actual harvester>/`
2. `make .venv`
3. `source .venv/bin/activate`
4. `python <actual harvester>.py`

## Non technical

### What

A self contained service which based on an environment will print out all the
APIs associated with the configured environment

### How

Each harvester runs in a docker container and pipes it's output to a
PVC. The output must conform to
[this](https://github.com/oslokommune/devportal-harvest-poc/blob/master/docs/standard_json.json) structure.

### Configuration

What environment variables are necessary depends on the harvester, but they all
have the following variables required:

* `SOURCE_NAME` the name of the publisher of the source. For example,
	Bymiljøetaten
* `SOURCE_IDENTIFIER` an url to data representing the source. It is adviced to
	use BRREG's json representation of the organization
