import os
import json
import sys

if len(sys.argv) > 1:
    json_path = sys.argv[1]
    if os.path.exists(json_path):
        file = open(json_path, "r")
        json = json.load(file)
        file.close()
        print("JSON IS VALID!")
        print(json)
    else:
        print(sys.argv[1] + " not found!")
else:
    print("Usage: python json_checker.py <json_file>")
