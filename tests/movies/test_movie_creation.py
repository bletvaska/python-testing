import pytest


def test_when_movie_is_created_then_http_status_code_should_be_201(movie):
    assert movie.status_code == 201


@pytest.mark.parametrize("key", ["objectId", "createdAt"])
def test_when_movie_is_created_then_it_should_pass_through_jsonschema_validation(movie, key):
    assert key in movie.json()
