import requests


def test_when_request_without_keys_then_expect_status_code_401(base_url):
    # arrange
    url = f"{base_url}/classes/movies"
    expected = 401

    # act
    response = requests.get(url)

    # assert
    assert response.status_code == expected


def test_when_request_without_keys_then_expect_error_message(base_url):
    # arrange
    url = f"{base_url}/classes/movies"
    expected = {"error": "unauthorized"}

    # act
    response = requests.get(url)

    # assert
    assert response.json() == expected


def test_when_valid_parse_app_id_was_provided_then_expect_status_code_403(base_url, headers):
    # arrange
    url = f"{base_url}/classes/movies"
    headers = {"X-Parse-Application-Id": headers['X-Parse-Application-Id']}
    expected = 403

    # act
    response = requests.get(url, headers=headers)

    # assert
    assert response.status_code == expected


def test_when_valid_parse_app_id_was_provided_then_expect_error_message(base_url, headers):
    # arrange
    url = f"{base_url}/classes/movies"
    headers = {"X-Parse-Application-Id": headers['X-Parse-Application-Id']}
    expected = {"error": "unauthorized"}

    # act
    response = requests.get(url, headers=headers)

    # assert
    assert response.json() == expected


def test_when_invalid_parse_app_id_was_provided_then_expect_status_code_401(faker, base_url):
    # arrange
    url = f"{base_url}/classes/movies"
    headers = {"X-Parse-Application-Id": faker.password()}
    expected = 401

    # act
    response = requests.get(url, headers=headers)

    # assert
    assert response.status_code == expected


def test_when_invalid_parse_app_id_was_provided_then_expect_error_message(faker, base_url):
    # arrange
    url = f"{base_url}/classes/movies"
    headers = {"X-Parse-Application-Id": faker.password()}
    expected = {"error": "unauthorized"}

    # act
    response = requests.get(url, headers=headers)

    # assert
    assert response.json() == expected
