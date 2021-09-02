import os
import requests as api

url = "https://jsonplaceholder.typicode.com/users"
response = api.get(url)
print(response.json())
