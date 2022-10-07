import requests

endpoint = "http://localhost:8000/api/products/45443434 "
get_response = requests.get(endpoint)
print(get_response.json())

