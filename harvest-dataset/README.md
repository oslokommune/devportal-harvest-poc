# Dataplatform dataset harvester

This service retrieves datasets from Oslo Kommune Data platform and stores it for later retrieval by other services.

## Technical

### Production

#### Setup
1. `git clone git@github.com:oslokommune/devportal-harvest-poc.git`
2. `kubectl apply -f charts/harvest-output-pvc.yaml` This is the PVC where all
	 the harvesters will pipe their output to.

#### Deploy harvest jobs

```bash
make deploy
```

This can also be used when updating after code changes.

### Local

1. `make init`
1. `source .venv/bin/activate`
1. `make run`

### Configuration

Set `DATASET_API_BASE_URL` to the base URL of the API that provides datasets. It's set in the files `.env` and
`harvest_job.yaml`.
