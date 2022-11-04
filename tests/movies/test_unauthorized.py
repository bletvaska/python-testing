import requests


def test_when_request_without_keys_then_expect_status_code_401():
    # arrange
    url = "https://parseapi.back4app.com/classes/movies"
    expected = 401

    # act
    response = requests.get(url)

    # assert
    assert response.status_code == expected


def test_when_request_without_keys_then_expect_error_message():
    # arrange
    url = "https://parseapi.back4app.com/classes/movies"
    expected = {"error": "unauthorized"}

    # act
    response = requests.get(url)

    # assert
    assert response.json() == expected


def test_when_valid_parse_app_id_was_provided_then_expect_status_code_403():
    # arrange
    url = "https://parseapi.back4app.com/classes/movies"
    headers = {"X-Parse-Application-Id": "axACcyh0MTO3z42rUN8vFHfyAgE22VRjd3IJOwlJ"}
    expected = 403

    # act
    response = requests.get(url, headers=headers)

    # assert
    assert response.status_code == expected


def test_when_valid_parse_app_id_was_provided_then_expect_error_message():
    # arrange
    url = "https://parseapi.back4app.com/classes/movies"
    headers = {"X-Parse-Application-Id": "axACcyh0MTO3z42rUN8vFHfyAgE22VRjd3IJOwlJ"}
    expected = {"error": "unauthorized"}

    # act
    response = requests.get(url, headers=headers)

    # assert
    assert response.json() == expected
