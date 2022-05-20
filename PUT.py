import requests
import json
url = "https://reqres.in/api/users?page=2"
file = open("payload.json", "r")
f1 = file.read()

response = requests.put(url , f1)

print(response.text)
print(response.content)

print(response.headers)
print(response.headers.get("content-Type"))
print(response.status_code)
print(type(response))
print(response)






