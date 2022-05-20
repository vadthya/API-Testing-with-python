import requests
import json
import pytest

@pytest.fixture()
def startFunction():
    global url
    url= "https://reqres.in/api"


def test_GETAPI(startFunction):
    get_url= url+"/users?page=2"
    response= requests.get(get_url)
    assert response.status_code == 200
    print(response.content)
    print(response.headers)
    assert "content-Type" in response.headers
    response_text = response.text
    print(type(response_text))
    response_json = json.loads(response.text)
    print(response_json)


def test_POSTAPI(startFunction):
    post_url = url+"/users"
    file = open("payload.json", 'r')
    f= file.read()

    response= requests.post(post_url, file)
    assert response.status_code == 201
    print(response.content)
    print(response.headers)
    assert "content-Type" in response.headers
    response_text = response.text
    print(type(response_text))
    response_json = json.loads(response.text)
    print(response_json)



