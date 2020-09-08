# Dataset harvest aggregator

Similar to the [API-harvester](https://github.com/oslokommune/devportal-harvest-poc/tree/master/harvest), but
harvests datasets instead of APIs.

## What

This service adds visibility to previously harvested data sets.

### visibility.json

visibility.json is a file that specifies the visibility level of a dataset with a given identifier.

```json
{
	"<original name>": "<visibility level>",
	"example-api": "PUBLIC",
	"private-example-api": "PROTECTED",
	...
}
```

This determines if the dataset should end up in the `public.json` file or the
`protected.json` file. If the API is not found in `visibility.json`, it's hidden
from both files.

`public.json` is exposed by latest_provider as json and turtle. It is also used
by the distributors.

`protected.json` will be exposed to authorized users when authorization is
implemented.
