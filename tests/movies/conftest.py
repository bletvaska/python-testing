import pytest


@pytest.fixture(scope='session')
def base_url():
    yield "https://parseapi.back4app.com"


@pytest.fixture(scope='session')
def headers():
    yield {
        "X-Parse-Application-Id": "axACcyh0MTO3z42rUN8vFHfyAgE22VRjd3IJOwlJ",
        "X-Parse-REST-API-Key": "sQAPUPRNJg2GpZ9f0fXZaALSvekT7N2KmdM8kBWk",
    }
