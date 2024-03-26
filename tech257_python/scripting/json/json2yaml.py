import json
import os
import sys
import yaml

if len(sys.argv) > 2:
    json_file = sys.argv[1]
    if os.path.exists(json_file):
        file = open(json_file, "r")
        content = json.load(file)
        file.close()
    else:
        print(f"ERROR: {json_file} not found!")
        exit(1)
else:
    print("Usage: python json2yaml.py <source.json> <target.yaml>")
    exit(1)

# Process the conversion - Use yaml library

json_file = open(sys.argv[1], "r")
yaml_file = open(sys.argv[2], "w")

json_stream = json.load(json_file)
yaml_content = yaml.dump(json_stream)

# Save the conversion in a new file with the name of the second argument

yaml_file.write(yaml_content)
print(f"Successfully converted and saved to {sys.argv[2]}")
