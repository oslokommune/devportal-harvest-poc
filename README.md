# devportal-harvest-poc

## Setup
1. `git clone git@github.com:oslokommune/devportal-harvest-poc.git`
2. `make init`
3. `make create-dotenv-file`

## Configure
Edit the created .env file to your liking and run `export $(cat .env)`

## Usage
`cat sources.yaml | python ctl.py`

This command generates a k8s cronjob for each of the specified harvesters. An
example of a sources.yaml file can be found
[here](https://github.com/oslokommune/devportal-harvest-poc/blob/master/docs/sources_template.yaml)

## Deploy harvesters

1. kubectl apply -f charts/harvest-output-pvc. This is the PVC where all the
	 harvesters will pipe their output and the latest_provider will read from
2. `make build`
3. Create and configure a [sources.yaml](https://github.com/oslokommune/devportal-harvest-poc/blob/master/docs/sources_template.yaml)
4. Run the step in Usage

## Deploy latest_provider

1. `cd tools/latest_provider`
2. `make deploy-test`

## [Roadmap](https://github.com/oslokommune/devportal-harvest-poc/projects/1?add_cards_query=is%3Aopen)
