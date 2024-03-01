import pytest
import requests


@pytest.mark.wip
def test_when_valid_movieid_and_credentials_then_status_code_is_200():
    # arrange
    url = 'https://parseapi.back4app.com/classes/movies/RrLTiBbILH'
    headers = {
        'X-Parse-Application-Id': 'axACcyh0MTO3z42rUN8vFHfyAgE22VRjd3IJOwlJ',
        'X-Parse-REST-API-Key': 'sQAPUPRNJg2GpZ9f0fXZaALSvekT7N2KmdM8kBWk'
    }

    # act
    response = requests.get(url, headers=headers, verify=False)

    # assert
    assert response.status_code == 200, 'Response status code is not 200'
