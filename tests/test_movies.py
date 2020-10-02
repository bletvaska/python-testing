import requests


class TestMovies:

    def test_when_no_credentials_are_provided_then_status_code_is_401(self, base_url):
        response = requests.get(base_url)
        assert response.status_code == 401

    def test_when_no_credentials_then_response_is_unauthorized(self, base_url):
        response = requests.get(base_url)
        assert response.json() == {'error': 'unauthorized'}

    def test_when_credentials_are_provided_then_status_code_is_200(self, base_url, headers):
        response = requests.get(base_url, headers=headers)
        assert response.status_code == 200

    def test_when_credentials_are_provided_then_exist_result(self, base_url, headers):
        response = requests.get(base_url, headers=headers)
        data = response.json()
        assert 'results' in data

    def test_when_credentials_are_provided_then_exist_result_as_list(self, base_url, headers):
        response = requests.get(base_url, headers=headers)
        assert type(response.json()['results']) == list

    def test_when_credentials_are_provided_then_exist_result_more_than_0(self, base_url, headers):
        response = requests.get(base_url, headers=headers)
        assert len(response.json()['results']) > 0
