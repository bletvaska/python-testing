import pytest


class TestMovie:
    @pytest.mark.parametrize('key', ['objectId', 'title', 'year', 'genres', 'createdAt', 'updatedAt'])
    def test_when_credentials_are_provided_then_scheme_is_valid(self, session, base_url, headers, key):
        response = session.get(f'{base_url}/VRt7KjXRCo', headers=headers)
        movie = response.json()
        assert key in movie

    def test_when_single_movie_is_requested_then_status_code_is_200(self, session, base_url, headers):
        response = session.get(f'{base_url}/VRt7KjXRCo', headers=headers)
        assert response.status_code == 200

    def test_when_new_movie_is_created_then_status_code_is_201(self, session, base_url, headers):
        payload = {
            'title': 'Suchá handra na dne morskom',
            'year': 1988,
            'genres': ['Drama', 'Mocny', 'Family'],
        }

        response = session.post(base_url, json=payload, headers=headers)
        print(response.json())

        assert response.status_code == 201
