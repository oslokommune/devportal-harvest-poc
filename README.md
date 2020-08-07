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

## [Roadmap](https://github.com/oslokommune/devportal-harvest-poc/projects/1?add_cards_query=is%3Aopen)
