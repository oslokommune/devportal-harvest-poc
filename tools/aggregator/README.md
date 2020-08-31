# Harvest aggregator

## Chart describing the aggregators role
[Chart](https://github.com/oslokommune/devportal-harvest-poc/blob/master/tools/aggregator/docs/aggregator.png)

## What
This service enriches the data harvested by the following means:

### name.json
```json
{
	"<original name": "<new name>",
	"example-api": "Amazing API",
	...
}
```

This renames the harvested api from `<original name>` to `<new name>`.

### description.json
```json
{
	"<original name>": "<description",
	"example-api": "This API blows your mind.",
	...
}
```

This adds a description to the harvested api.

### specificationURL.json
```json
{
	"<original name>": "<specification url>",
	"example-api": "https://awesome.no/spec",
	...
}
```

This adds a specification url to the harvested api.

### visibility.json
```json
{
	"<original name>": "<visibility level>",
	"example-api": "PUBLIC",
	"private-example-api": "PROTECTED",
	...
}
```

Determines if the API should end up in the `public.json` file or the
`protected.json` file. If the API is not found in `visibility.json`, it's hidden
from both files.

`public.json` is exposed by latest_provider as json and turtle. It is also used
by the distributors.
`protected.json` will be exposed to authorized users when authorization is
implemented
