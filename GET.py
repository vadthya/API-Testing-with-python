import requests
import json

url = "https://reqres.in/api/users?page=2"
response = requests.get(url)
print(response.headers)
print(response.text)
assert response.status_code == 200
assert "content-Type" in response.headers
test = response.text
print("type of response ", type(response))

print("Validated sucessfully")

## converting text to json format

response_json = json.loads(response.text)
print("type of response after converting to json", type(response_json))
print(response_json)
print(response.text)

## to print the total pages.
total = response_json['total_pages']
print(total)
assert total == 2
print("The request is of two pages")

#### Accessing the data
name = response_json['data'][1]['first_name']
print(name)

print(len(response_json['data']))
info = response_json['data']
print(info)

### printing the list of links and first names
count = 0
list = []

while count < len(response_json):
    for i in info:
        list.append(i['first_name'])
        count = count + 1
    print(list)


