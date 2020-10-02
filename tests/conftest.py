import pytest
import requests


@pytest.fixture(scope='session')
def base_url():
    """
    Provides base url for request.
    """
    return 'https://parseapi.back4app.com/classes/movies'


@pytest.fixture(scope='session')
def headers():
    return {
        'X-Parse-Application-Id': 'axACcyh0MTO3z42rUN8vFHfyAgE22VRjd3IJOwlJ',
        'X-Parse-REST-API-Key': 'sQAPUPRNJg2GpZ9f0fXZaALSvekT7N2KmdM8kBWk'
    }


@pytest.fixture(scope='class')
def session():
    session = requests.Session()
    yield session
    session.close()


@pytest.fixture(scope='class')
def new_movie():
    payload = {
        'title': 'Suchá handra na dne morskom',
        'year': 1988,
        'genres': ['Drama', 'Mocny', 'Family'],
    }

    response = session.post(base_url, json=payload, headers=headers)
    data = response.json()
    payload['objectId'] = data['objectId']
    payload['createdAt'] = data['createdAt']

    yield payload

    session.delete(f'{base_url}/{payload.objectId}', headers=headers)
