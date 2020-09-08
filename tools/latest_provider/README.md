# Latest Provider

## What

A service which exposes the following endpoints:
* GET /apis: Returns APIs from a central storage as JSON or Turtle, depending on accept headers.
* GET /datasets: Returns datasets from a central storage as JSON or Turtle, depending on accept headers.

## Testing locally

```bash
make build-image run-docker VERSION=test

curl -H "accept: application/json" http://localhost:5000/apis
curl -H "accept: text/turtle" http://localhost:5000/apis

curl -H "accept: application/json" http://localhost:5000/datasets
curl -H "accept: text/turtle" http://localhost:5000/datasets
```
