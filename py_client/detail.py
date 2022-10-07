import requests

endpoint = "http://localhost:8000/api/products/4/"

get_response = requests.get(endpoint, json={"title":"Hello world"})
# print(get_response.text)

print(get_response.json())
# print(get_response.status_code)
