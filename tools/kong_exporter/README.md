# Kong Exporter

## What

A service that uses the Kong Admin API to extract all existing services and
expose them on /apis. Due to security concerns, this service runs on Kong's
localhost and is exposed through Kong with an API key.

## Deployment

1. `make build` and `make push`
2. ssh into the Kong server and run `docker run --network host `container-registry.oslo.kommune.no/kong-api-exporter`
