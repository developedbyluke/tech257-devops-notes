import requests
import json

# SINGLE POSTCODE

response = requests.get("https://api.postcodes.io/postcodes/se120nb")

data = response.json()['result']
print(f"{data['postcode']}\nPolice force: {data['pfa']}\n")


# MULTIPLE POSTCODES

body = json.dumps({
    "postcodes": ["NG13 8FA", "PR3 0SG", "M45 6GN", "EX16 5BL"]
})

response = requests.post("https://api.postcodes.io/postcodes", data=body, headers={"Content-Type": "application/json"})

data = response.json()['result']
for item in data:
    data = item['result']
    print(f"{data['postcode']}\nPolice force: {data['pfa']}\n")
