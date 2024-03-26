import sys
import yaml

stream = open(sys.argv[1], "r")
data = yaml.safe_load(stream)

for key in data:
    print(f"The key is {key} and the value is {data[key]}")
