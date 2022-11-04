import json
from jsonschema import validate
import pytest


def test_when_request_without_keys_then_expect_status_code_401(base_url, session):
    # arrange
    url = f"{base_url}/classes/movies/WHyejDIzEv"
    expected = 401

    # act
    response = session.get(url)

    # assert
    assert response.status_code == expected


def test_when_valid_keys_are_provided_then_expect_status_code_200(base_url, headers, session):
    # arrange
    url = f"{base_url}/classes/movies/WHyejDIzEv"
    expected = 200

    # act
    response = session.get(url, headers=headers)

    # assert
    assert response.status_code == expected


def test_when_valid_keys_are_provided_then_expect_content_of_type_json(base_url, headers, session):
    # arrange
    url = f"{base_url}/classes/movies/WHyejDIzEv"

    # act
    response = session.get(url, headers=headers)

    # assert
    assert response.headers["Content-Type"].startswith("application/json")


@pytest.mark.parametrize("key", ["objectId", "title", "year", "genres", "createdAt", "updatedAt"])
def test_when_valid_keys_are_provided_then_expect_keys_in_json(base_url, headers, key, session):
    # arrange
    url = f"{base_url}/classes/movies/WHyejDIzEv"

    # act
    response = session.get(url, headers=headers)

    # assert
    assert key in response.json()


def test_when_movie_is_returned_then_it_should_pass_through_jsonschema_validation(base_url, headers, session, movie_schema):
    # arrange
    url = f"{base_url}/classes/movies/WHyejDIzEv"
    response = session.get(url, headers=headers)
    instance = response.json()

    # act / assert
    validate(instance=instance, schema=movie_schema)
