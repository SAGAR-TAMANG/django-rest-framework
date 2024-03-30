import requests

product_id = int(input("What product ID do you want to delet?"))

endpoint = f"http://localhost:8000/api/products/{product_id}/delete/"

get_response = requests.delete(endpoint)

print("DELETE Done")