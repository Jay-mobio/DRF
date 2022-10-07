import requests

headers = {'Authorization': 'Bearer 093fd3c814bf6ece4651611b0b5335d6ddf37ca1'}
endpoint = "http://localhost:8000/api/products/"

data = {
    "title":"This feild is done",
    "price":32.99
}
get_response = requests.post(endpoint, json = data,headers=headers)
print(get_response.json())

