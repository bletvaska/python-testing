import pytest
import requests

url = 'https://parseapi.back4app.com/classes/movies'


class TestMovie:
    movie_id: str = 'RrLTiBbILH'

    @pytest.fixture
    def headers(self):
        yield {
            'X-Parse-Application-Id': 'axACcyh0MTO3z42rUN8vFHfyAgE22VRjd3IJOwlJ',
            'X-Parse-REST-API-Key': 'sQAPUPRNJg2GpZ9f0fXZaALSvekT7N2KmdM8kBWk'
        }

    def test_when_valid_movieid_and_credentials_then_status_code_is_200(self, headers):
        response = requests.get(f'{url}/{self.movie_id}', headers=headers, verify=False)
        assert response.status_code == 200, 'Response status code is not 200'

    def test_when_valid_movieid_and_credentials_then_content_type_is_json(self, headers):
        response = requests.get(f'{url}/{self.movie_id}', headers=headers)
        assert 'application/json' in response.headers['content-type'], 'Response is not JSON document.'
