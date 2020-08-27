# Proof of concept for harvesting and distributing API metadata

[Data flow diagram](docs/data-flow.vpd.png)

## Harvest
More information regarding harvesting can be found [here](https://github.com/oslokommune/devportal-harvest-poc/tree/master/harvest)

## Distribute
More information regarding distribution can be found [here](https://github.com/oslokommune/devportal-harvest-poc/tree/master/distribute)

## Preparation
kubectl apply -f charts/harvest-output-pvc. This is the PVC where all the
harvesters will pipe their output to and where the latest_provider and distributors will read from

## Stack
Based on a [sources.yaml](https://github.com/oslokommune/devportal-harvest-poc/blob/master/harvest/templates/sources_template.yaml)
file, the harvest.py script will generate cronjobs that will pipe their output
to a persistent volume.

The latest_provider service will upon a GET request to /apis expose the sum of all the
.json files in the mentioned persistent volume claim.

The harvester frontend does a GET /apis to the latest_provider service and presents
the result.

## [Roadmap](https://github.com/oslokommune/devportal-harvest-poc/projects/1?add_cards_query=is%3Aopen)
