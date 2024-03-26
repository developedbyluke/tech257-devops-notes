import requests

response = requests.get('https://dogapi.dog/api/v2/breeds')

data = response.json()

print(data['data'][0]['attributes']['name'])
