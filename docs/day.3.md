# Day 3: Rest API Testing

Introduction to Requests: HTTP for Humans
je potrebné nainštalovať balíček request a httpie pre testovanie

```bash
pip install requests httpie
```


nainštalovať aspoň rozšírenie pre Chrome/Chromium s názvom Postman

## Anatomy of HTTP Request

## Anatomy of HTTP Response

## HTTP Client from CLI

mame niekolko nastrojov. z prikazoveho riadku vieme pouzit httpie:

```bash
$ http https://parseapi.back4app.com/classes/artists/ \
  X-Parse-Application-Id:fG4xbiuMg3nXmkiaVOoEd0KhwFLn0B8RX3dO9T2V \
  X-Parse-REST-API-Key:fHofHzmvUXYE2sITHC9eFOQnovsIFOqUGTglxDge
```

alebo v linuxovych systemoch nastroj `curl`:

```bash
$ curl -X GET https://parseapi.back4app.com/classes/artists/ \
-H "X-Parse-Application-Id: fG4xbiuMg3nXmkiaVOoEd0KhwFLn0B8RX3dO9T2V" \
-H "X-Parse-REST-API-Key: fHofHzmvUXYE2sITHC9eFOQnovsIFOqUGTglxDge" | json_reformat
```

## Working with requests

### Retrieving Data

Získajte zoznam všetkých artistov (endpoint: artists/)

```python
url = 'https://parseapi.back4app.com/classes/artists/'
headers = {'X-Parse-Application-Id': 'fG4xbiuMg3nXmkiaVOoEd0KhwFLn0B8RX3dO9T2V',
           'X-Parse-REST-API-Key': 'fHofHzmvUXYE2sITHC9eFOQnovsIFOqUGTglxDge'}
result = requests.get(url, headers=headers)

print(result.status_code)
# 200: OK
print(result.json())
```

Získajte záznam o umelcovi s id objectId=2p6AcefQAX

```python
url = 'https://parseapi.back4app.com/classes/artists/2p6AcefQAX'
headers = {'X-Parse-Application-Id': 'fG4xbiuMg3nXmkiaVOoEd0KhwFLn0B8RX3dO9T2V',
           'X-Parse-REST-API-Key': 'fHofHzmvUXYE2sITHC9eFOQnovsIFOqUGTglxDge'}
result = requests.get(url, headers=headers)

print(result.status_code)
# 200: OK
print(result.json())
```


Získajte záznam o umelcovi s menom Richard Müller

```python
url = 'https://parseapi.back4app.com/classes/artists?where={"name":"Richar Müller"}'
headers = {'X-Parse-Application-Id': 'fG4xbiuMg3nXmkiaVOoEd0KhwFLn0B8RX3dO9T2V',
           'X-Parse-REST-API-Key': 'fHofHzmvUXYE2sITHC9eFOQnovsIFOqUGTglxDge'}
result = requests.get(url, headers=headers)

print(result.status_code)
# 200: OK
print(result.json())
```

### Creating Data

Vytvorte nového umelca s menom Richard Müller.

```python
url = 'https://parseapi.back4app.com/classes/artists/'
headers = {'X-Parse-Application-Id': 'fG4xbiuMg3nXmkiaVOoEd0KhwFLn0B8RX3dO9T2V',
           'X-Parse-REST-API-Key': 'fHofHzmvUXYE2sITHC9eFOQnovsIFOqUGTglxDge'}
payload = {'name': 'Richard Müller'}
result = requests.post(url, json=payload, headers=headers)

print(result.status_code)
# 201: Created
print(result.json())
```


### Deleting Data

Odstráňte vytvorený záznam o umelcovi s menom Richard Müller.

```python
url = 'https://parseapi.back4app.com/classes/artists?where={"name":"Richard Müller"}'
headers = {'X-Parse-Application-Id': 'fG4xbiuMg3nXmkiaVOoEd0KhwFLn0B8RX3dO9T2V',
           'X-Parse-REST-API-Key': 'fHofHzmvUXYE2sITHC9eFOQnovsIFOqUGTglxDge'}
result = requests.delete(url, headers=headers)

print(result.status_code)
# 200: OK
print(result.json())
```


### Updating Data


## Testing REST API with requests

Štruktúra testov na súborovom systéme:

```
pytesters
└── test/
    ├── conftest.py
    └── test_movies.py
```

V súbore `conftest.py` sa nachádzajú napríklad fixtures, ktoré sa budú v testoch používať:

```python
import pytest
import requests


@pytest.fixture(scope="class")
def headers():
    return {'X-Parse-Application-Id': 'fG4xbiuMg3nXmkiaVOoEd0KhwFLn0B8RX3dO9T2V',
            'X-Parse-REST-API-Key': 'fHofHzmvUXYE2sITHC9eFOQnovsIFOqUGTglxDge'}


@pytest.fixture(scope="class")
def session():
  return requests.session()


@pytest.fixture(scope="class")
def base_url():
  return 'https://parseapi.back4app.com/classes/movies'
```

Samotné testy organizované v triedach (ako test case-y):

```python
class TestMovies:
  def test_when_no_credits_are_provided_then_return_401(self, session, base_url):
    response = session.get(base_url)
    assert response.status_code == 401

  def test_when_invalid_credentials_are_provided_then_return_500(self, session, base_url):
    headers = {'X-Parse-Application-Id': 'invalid',
               'X-Parse-REST-API-Key': 'invalid'}
    response = session.get(base_url, headers=headers)
    assert response.status_code == 500

  def test_when_valid_credentials_are_provided_then_return_200(self, session, headers, base_url):
    response = session.get(base_url, headers=headers)
    assert response.status_code == 200
```


## Links

* http://docs.python-requests.org/en/master/
* https://httpstatuses.com/
* https://www.back4app.com/
* https://www.youtube.com/watch?v=mZ8_QgJ5mbs
* http://naucse.python.cz/lessons/intro/requests/
* http://httpbin.org/
* HTTP primer for frontend developers

