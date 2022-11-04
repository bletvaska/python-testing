import json
import pytest
import requests


@pytest.fixture(scope="session")
def base_url():
    yield "https://parseapi.back4app.com"


@pytest.fixture(scope="session")
def headers():
    yield {
        "X-Parse-Application-Id": "axACcyh0MTO3z42rUN8vFHfyAgE22VRjd3IJOwlJ",
        "X-Parse-REST-API-Key": "sQAPUPRNJg2GpZ9f0fXZaALSvekT7N2KmdM8kBWk",
    }


@pytest.fixture(scope="module")
def session():
    # session = requests.session()
    # yield session
    # session.close()

    with requests.session() as session:
        yield session


@pytest.fixture(scope="module")
def movie(base_url, headers, session):
    # setup
    payload = {"title": "The Fabelmans", "year": 2022, "genres": ["Drama"]}

    result = session.post(f"{base_url}/classes/movies", headers=headers, json=payload)
    data = result.json()

    yield result

    # teardown
    session.delete(f"{base_url}/classes/movies/{data['objectId']}", headers=headers)


@pytest.fixture(scope='session')
def movie_schema():
    with open("tests/movies/movie.schema.json") as file:
        schema = json.load(file)

    yield schema
