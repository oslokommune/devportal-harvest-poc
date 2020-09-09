import json
import sys

from datacatalogtordf import Catalog, Dataset

BASE_URL = "https://apis.k8s-test.oslo.kommune.no/katalog/data" # TODO: Get from env

catalog = Catalog()
catalog.identifier = "https://apis.k8s-test.oslo.kommune.no/katalog/data"
catalog.title = {
    "no": "Oslo Kommunes datasettkatalog",
    "en": "The dataset catalog of municipality of Oslo"
}
catalog.publisher = "https://w2.brreg.no/enhet/sok/detalj.jsp?orgnr=920204368"

data = json.loads(sys.stdin.read())

for item in data:
    dataset = Dataset()
    dataset.identifier = f"{BASE_URL}/{item['identifier']}"
    dataset.title = { "nb": item["title"] }
    dataset.description = { "nb": item.get("description", "") }
    # Needs to be an URI, while now it's just a string. Figure out later how to deal with this.
    # dataset.publisher = item.get("publisher", "")

    catalog.datasets.append(dataset)

rdf = catalog.to_rdf()
print(rdf.decode())
