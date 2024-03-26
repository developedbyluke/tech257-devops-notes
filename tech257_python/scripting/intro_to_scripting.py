import sys
import os
import subprocess
import json

# os
# os.mkdir("test-dir")

# sys
if len(sys.argv) > 1:
    print("You gave me an argument!")

# json
x = {
    "name": "John",
    "age": 24,
    "city": "Liverpool"
}

y = json.dumps(x)

print(type(x))
print(type(y))
