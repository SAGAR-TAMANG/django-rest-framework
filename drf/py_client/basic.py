import requests 

endpoint = "http://localhost:8000/api/"

get_response = requests.post(endpoint, json={"title": "ABC123", "value": "Hello World", "price": None} )
print(get_response.json())