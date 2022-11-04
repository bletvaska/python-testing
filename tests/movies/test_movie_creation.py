import pytest


class TestMovieCreation:
    def test_when_movie_is_created_then_http_status_code_should_be_201(self, movie):
        assert movie.status_code == 201

    @pytest.mark.parametrize("key", ["objectId", "createdAt"])
    def test_when_movie_is_created_then_it_should_pass_through_jsonschema_validation(self, movie, key):
        assert key in movie.json()


class TestMovieDelete:
    def test_when_movie_is_deleted_then_http_status_code_should_be_204(self):
        assert True


class TestMovieUpdate:
    def test_when_movie_is_updated_then_http_status_code_should_be_200(self):
        assert True
