import requests

endpoint = "http://localhost:8000/api/products/"

headers = {
  'Authorization': 'Bearer 02fdb7bfdd6b4a740fc23839772ecb3697879d62'
}

data = {
  "title" : "another one",
  "price" : 101,
}

get_response = requests.post(endpoint, json=data, headers = headers)

print(get_response.json())