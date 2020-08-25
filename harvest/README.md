# Harvester

## What

A self contained service which based on an environment will print out all the
APIs associated with the configured environment

## How

Each harvester runs in a docker container and pipes it's output to a
PVC. The output must conform to
[this](https://github.com/oslokommune/devportal-harvest-poc/blob/master/docs/standard_json.json) structure.

## Configuration

What environment variables are necessary depends on the harvester, but they all
have the following variables required:

* `SOURCE_NAME` the name of the publisher of the source. For example,
	Bymiljøetaten
* `SOURCE_IDENTIFIER` an url to data representing the source. It is adviced to
	use BRREG's json representation of the organization
