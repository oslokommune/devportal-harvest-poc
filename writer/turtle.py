import json
import sys
from rdflib import URIRef, Graph, Literal, RDF, BNode
from rdflib.namespace import DCAT, DCTERMS, FOAF

from datacatalogtordf import Catalog, DataService

data = json.loads(sys.stdin.read())

g = Graph()
g.bind('dcat', DCAT)
g.bind('dct', DCTERMS)
g.bind('foaf', FOAF)

catalog = URIRef('920204368')

g.add((catalog, RDF.type, DCAT.Catalog))
g.add((
    catalog,
    DCTERMS.title,
    Literal('Oslo Kommunes API-katalog', lang='no')
))
g.add((
    catalog,
    DCTERMS.title,
    Literal('The Oslo Kommune API catalog', lang='en')
))
g.add((
    catalog,
    DCTERMS.publisher,
    URIRef('https://data.brreg.no/enhetsregisteret/api/enheter/920204368')
))
g.add((
    catalog,
    FOAF.homepage,
    Literal('https://www.oslo.kommune.no')
))

identifier = 0
for item in data:
    identifier += 1
    item['identifier'] = f'https://developer.oslo.kommune.no/katalog/api/{identifier}/'

    api = URIRef(item['identifier'])

    g.add((api, RDF.type, DCAT.DataService))
    g.add((api, DCTERMS.title, Literal(item['title'], lang='no')))
    g.add((api, DCTERMS.publisher, URIRef(item['publisher'])))

    g.add((catalog, DCAT.service, api))

print(g.serialize(format='turtle').decode())
