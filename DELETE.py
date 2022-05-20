import requests
url = "https://reqres.in/api/users?page=2"
response= requests.delete(url)
print(response.content)
assert response.status_code==204
print("deleted successfully")