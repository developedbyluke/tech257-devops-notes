import os
import json

path = "example.json"

json = json.loads(open(path).read())

for key in json:
    value = json[key]
    print(f"The key is {key} and the value is {value}")
