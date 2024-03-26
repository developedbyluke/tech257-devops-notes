import urllib.request
import requests
import json

with urllib.request.urlopen("http://jsonplaceholder.typicode.com/todos/1") as url:
    data = json.load(url)
    print(data)

response = requests.get("http://jsonplaceholder.typicode.com/todos/1")
data = response.text
print(data)
