import os
import yaml
import sys

if len(sys.argv) > 1:
    yaml_path = sys.argv[1]
    if os.path.exists(yaml_path):
        file = open(yaml_path, "r")
        yaml = yaml.safe_load(file)
        file.close()
        print("YAML IS VALID!")
        print(yaml)
    else:
        print(sys.argv[1] + " not found!")
else:
    print("Usage: python json_checker.py <json_file>")
