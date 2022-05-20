import requests
import json
url = "https://reqres.in/api/users"
file = open("payload.json", 'r')
f1 = file.read()



response = requests.post(url, f1)
print(response.text)

response_json= json.loads(response.text)
print(response_json)

print(response)
print(response.content)

print(response.headers)
print(response.headers.get("content-Type"))
print(response.status_code)
print(type(response))
print(response)










