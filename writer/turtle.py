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

identifier = 0
for item in data:
    identifier += 1
    item['identifier'] = f'https://developer.oslo.kommune.no/katalog/api/{identifier}/'

    api = DataService()
    api.title = {'nb': item['title']}
    api.identifier = item['identifier']

    catalog.services.append(api)

print(catalog.to_rdf().decode())
