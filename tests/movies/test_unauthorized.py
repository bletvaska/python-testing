import requests


def test_when_request_without_keys_then_expect_status_code_401():
    # arrange
    url = 'https://parseapi.back4app.com/classes/movies'

    # act
    response = requests.get(url)

    # assert
    assert response.status_code == 401


def test_when_request_without_keys_then_expect_error_message():
    # arrange
    url = 'https://parseapi.back4app.com/classes/movies'
    expected = {'error': 'unauthorized'}

    # act
    response = requests.get(url)

    # assert
    assert response.json() == expected
