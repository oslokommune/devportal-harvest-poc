import json
import sys
import urllib.parse
from rdflib import URIRef, Graph, Literal, RDF, BNode
from rdflib.namespace import DCAT, DCTERMS, FOAF

data = json.loads(sys.stdin.read())

g = Graph()
g.bind('dcat', DCAT)
g.bind('dct', DCTERMS)
g.bind('foaf', FOAF)

catalog = URIRef('https://harvester-frontend.k8s-test.oslo.kommune.no')

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

for item in data:
    item['identifier'] = 'https://harvester-frontend.k8s-test.oslo.kommune.no/katalog/api/'
    item['identifier'] += urllib.parse.quote(item['title'])

    api = URIRef(item['identifier'])

    g.add((api, RDF.type, DCAT.DataService))
    g.add((api, DCTERMS.title, Literal(item['title'], lang='no')))
    g.add((api, DCTERMS.publisher, URIRef(item['publisher'])))

    g.add((catalog, DCAT.service, api))

print(g.serialize(format='turtle').decode())
