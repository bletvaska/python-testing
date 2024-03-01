# Day 3: Rest API Testing

## Morning Excercise: Testing of Login Form

Otestujte prihlasovaci formular na adrese [https://www.dsl.sk/user.php?action=login](https://www.dsl.sk/user.php?action=login) Prihlasovacie meno a heslo pre otestovanie uspesneho prihlasenia je `pytester:pytester`. **Prosim nemenit!**

zistit aktualnu stranku je mozne pomocou: `driver.current_url`

* **ak** zadam spravny login a spravne heslo **tak** ma presmeruje na stranku [https://www.dsl.sk/](https://www.dsl.sk/).
* **ak** zadam nespravny login a nespravne heslo **tak** zostanem na rovnakej stranke.
* **ak** zadam login ale nespravne heslo, **tak** zostanem na rovnakej stranke.
* **ak** zadam spravny login ale nespravne heslo, **tak** zostanem na rovnakej stranke.
* **ak** zadam login ale nezadam heslo, **tak** zostanem na rovnakej stranke.
* **ak** odoslem prazdny formular, **tak** sa dostanem na rovnakej stranke.


### Riešenie

```python
from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest


```


### Vytvorenie fixture pre prihláseného používateľa

```python
@pytest.fixture
def 
```


## Introduction to Requests: HTTP for Humans

je potrebné nainštalovať balíček `request` a `httpie` pre testovanie

```bash
$ pip install requests httpie
```


nainštalovať aspoň rozšírenie pre Chrome/Chromium s názvom Postman

## Anatomy of HTTP Request

![Anatomy of HTTP Request ([source](https://www.webdevdrops.com/en/http-primer-for-frontend-developers-f091a2070637/))](images/anatomy.of.http.request.png)


## Anatomy of HTTP Response

![Anatomy of HTTP Response ([source](https://www.webdevdrops.com/en/http-primer-for-frontend-developers-f091a2070637/))](images/anatomy.of.http.response.png)

## HTTP Client from CLI

mame niekolko nastrojov. z prikazoveho riadku vieme pouzit httpie:

```bash
$ http https://parseapi.back4app.com/classes/movies \
  X-Parse-Application-Id:axACcyh0MTO3z42rUN8vFHfyAgE22VRjd3IJOwlJ \
  X-Parse-REST-API-Key:sQAPUPRNJg2GpZ9f0fXZaALSvekT7N2KmdM8kBWk
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


## JSON Schema Validation

JSON vieme validovat syntakticky, ale nie semanticky

pre semanticku validaciu však existuje projekt JSON Schema a niekolko validatorov. jej specifikacia sa nachadza na adrese http://json-schema.org/

vytvoríme si teda JSON schemu pre validaciu záznamov o filmoch


### Creating JSON Schema

jeden z online validatorov sa nachadza na adrese https://www.jsonschemavalidator.net/

do pravej casti vlozime ukazkovy JSON dokument, na ktorom budeme nasu novu schemu skusat. staci zobrat lubovolny filmovy JSON dokument:

```json
{
  "objectId": "1M7MWSwXZm",
  "title": "Braveheart",
  "year": 1995,
  "genres": [
    "Action",
    "Drama",
    "War"
  ],
  "createdAt": "2019-12-02T11:59:18.682Z",
  "updatedAt": "2019-12-02T11:59:18.682Z"
}
```

ako pomocku mozeme pouzit tutorial zo stranky http://json-schema.org/, ktory sa nachadza v Learn > Getting Started Step-By-Step. Postupne mozeme vytvorit schemu pre nas JSON objekt pre film.

```json
{
  "$schema": "https://json-schema.org/draft/2019-09/schema",
  "title": "Movie",
  "description": "A movie info",
  "type": "object",
  "properties": {
    "objectId": {
      "description": "The unique identifier for a movie",
      "type": "string"
    },
    "title": {
      "description": "The title of the movie",
      "type": "string"
    },
    "year": {
      "description": "The year of release",
      "type": "integer",
      "minimum": 1880
    },
    "genres": {
      "description": "The list of genres",
      "type": "array",
      "items": {
            "type": "string",
           "enum": [
             "Action",
                "Drama",
             "War"
           ]
      },
      "uniqueItems": true
    },
    "createdAt": {
      "description": "The date and time of entry creation",
      "type": "string",
      "pattern": "^\\d{4}-\\d{2}-\\d{2}T\\d{2}:\\d{2}:\\d{2}\\.\\d{3}Z$"
    },
    "updatedAt": {
      "description": "The date and time of last entry update",
      "type": "string",
      "format": "date-time"
    }
  },
  "required": [
    "objectId",
    "title",
    "year",
    "genres",
    "createdAt",
    "updatedAt"
  ]
}
```

### JSON Schema Validation in Python

nainstalujeme si balik [`jsonschema`](https://python-jsonschema.readthedocs.io/en/stable/):

```bash
$ pip install jsonschema
```

z prikazoveho riadku mozeme ako JSON Schema Validator pouzit nastroj `jsonschema`.  vie pracovať so standardnym vstupom, ale aj so súborom. jeho pouzitie moze vyzerat takto:

```bash
$ jsonschema schema.json --instance document.json
```

v pripade, ze JSON dokument nezodpoveda scheme, dojde k zobrazeniu chybovej hlasky a nastaveniu exit statusu na hodnotu inu ako 0.

z kodu mozeme vyriesit validaciu takto:

```python
>>> from jsonschema import validate

>>> # A sample schema, like what we'd get from json.load()
>>> schema = {
...     "type" : "object",
...     "properties" : {
...         "price" : {"type" : "number"},
...         "name" : {"type" : "string"},
...     },
... }

>>> # If no exception is raised by validate(), the instance is valid.
>>> validate(instance={"name" : "Eggs", "price" : 34.99}, schema=schema)

>>> validate(
...     instance={"name" : "Eggs", "price" : "Invalid"}, schema=schema,
... )
Traceback (most recent call last):
    ...
ValidationError: 'Invalid' is not of type 'number'
```


## Mocking

* čo to je?


### Inštalácia

Pridať podporu je možné nainštalovaním modulu `pytest-mock`. To urobíme príkazom `pip`:

```bash
$ pip install pytest-mock
```

Ak používame `poetry`, tak to urobíme takto:

```bash
$ poetry add pytest-mock
```


### Príklad použitia

Budeme sa tváriť, že robíme aplikáciu na prácu s filmami


### Fixtures

```python
@pytest.fixture
def mock_get(mocker):
  mock = Mock()
  mocker.patch('requests.get', return_value = mock)
  return mock
```

použitie:

```python
def test_when_get_request_then_status_is_ok(mock_get):
  # arrange
  mock_get.return_value.status_code = 200

  # act
  response = requests.get('http://example.com')

  # assert
  assert response.status_code == 200


def test_when_get_request_then_response_is_json(mock_get):
  # arrange
  mock_get.return_value.json.return_value = {'key': 'value'}

  # act
  response = requests.get('http://example.com')

  # assert
  assert response.json() == {'key': 'value'}
```


## Paralelné spúšťanie testov

Aktuálne sa testy spúšťajú sekvenčne - každý test sa spustí až po vykonaní predchádzajúceho testu. To samozrejme môže viesť ku veľmi dlhému trvaniu pre vykonanie celej sady testov. A ak sa budeme držať základných pravidiel testovania, minimálne sady testov, ale rovnako tak mnohé jednotkové testy samotné, by sme mali vedieť spúšťať aj paralelne.

Ak chceme zabezpečiť paralelný beh jednotlivých testov, potrebujeme nainštalovať ďalší modul. K dispozícii máme v podstate dva

* [`pytest-xdist`](https://pypi.org/project/pytest-xdist/)
* [`pytest-paralel`](https://pypi.org/project/pytest-parallel/)

My nainštalujeme ten prvý z nich:

```bash
$ poetry add pytest-xdist
```

Pri spúšťaní testov teraz môžeme pomocou voľby `--numprocesses` alebo skrátene `-n` určiť, na koľkých CPU sa majú testy spúšťať. Ak chceme spustiť testy napr. na troch CPU, spustíme ich takto:

```bash
$ pytest -n 3
```

Pomocou hodnoty `auto` zabezpečíme, že `pytest` spustí testy na toľkých CPU, koľko ich máme k dispozícii:

```bash
$ pytest -n auto
```

## Links

* [Requests: HTTP for Humans™](https://requests.readthedocs.io/en/latest/) - Domovská stránka modulu `requests`
* [Nauč se Python!: Requests](http://naucse.python.cz/lessons/intro/requests/)
* https://httpstatuses.com/
* https://www.back4app.com/
* https://www.youtube.com/watch?v=mZ8_QgJ5mbs
* http://httpbin.org/
* HTTP primer for frontend developers
* [`pytest-xdist`](https://pytest-xdist.readthedocs.io/en/stable/) - dokumentácia k rozšíreniue `pytest-xdist`
* [Page Object Models Implementation with Pytest](https://medium.com/@aifakhri/page-object-models-implementation-with-pytest-b9673744b8c0) - Building a well structured pytest test framework with Page Object Models
