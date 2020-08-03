import json
import sys

from datacatalogtordf import Catalog, DataService

data = json.loads(sys.stdin.read())

catalog = Catalog()
catalog.identifier = 'https://developer.oslo.kommune.no/katalog/api'
catalog.publisher = 'https://data.brreg.no/enhetsregisteret/oppslag/enheter/920204368'
catalog.title = {
    'en': 'The Oslo Kommune API catalog',
    'no': 'Oslo Kommunes API-katalog'
}

for item in data:
    item['identifier'] = 'https://developer.oslo.kommune.no/katalog/api/31/'

    api = DataService()
    api.title = {'nb': item['title']}
    api.identifier = item['identifier']

    catalog.services.append(api)

print(catalog.to_rdf().decode())
