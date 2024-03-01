import json
from pathlib import Path

import pytest


@pytest.fixture(scope='package')
def config():
    return {
        'username': 'pytester',
        'password': 'pytester'
    }


@pytest.fixture(scope='package')
def config_from_json():
    path = Path(__file__).parent / 'config.json'
    with open(path) as file:
        data = json.load(file)
        yield data
