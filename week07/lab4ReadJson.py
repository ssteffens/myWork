# This program reads in a dictionary object from a JSON file
# Author: Stefanie Steffens

import json
filename = "testdict.json"

def readDict():
    with open(filename, "rt") as f:
        return json.load(f)

somedict = readDict()
print(somedict)