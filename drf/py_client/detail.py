import requests

product_id = int(input("What product ID do you want to view?"))

endpoint = f"http://localhost:8000/api/products/{product_id}/"

get_response = requests.get(endpoint)

print(get_response.json())