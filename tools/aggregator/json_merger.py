import glob
import json
import os
import sys

folder = sys.argv[1]
files = os.listdir(folder)

apis = list()

for f in files:
    with open(os.path.join(folder, f)) as current:
        data = json.loads(current.read())

        apis += data

print(json.dumps(apis))
