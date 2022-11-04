import pytest


@pytest.fixture
def base_url():
    yield 'https://parseapi.back4app.com'
