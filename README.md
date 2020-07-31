# devportal-harvest-poc

## Setup
1. `git clone git@github.com:oslokommune/devportal-harvest-poc.git`
2. `make init`
3. `make create-dotenv-file`

## Configure
Edit the created .env file to your liking

## Usage
* `make harvest` will fetch apis from the harvesters in harvester/ and generate a data file in data/
* `make distribute` will upload the generated data file to the distributors in distributors/

## [Roadmap](https://github.com/oslokommune/devportal-harvest-poc/projects/1?add_cards_query=is%3Aopen)
