import pytest

from tests.pages.login_page import LoginPage


@pytest.mark.nondestructive
@pytest.mark.repeat(10)
def test_when_invalid_credentials_are_provided_then_error_message_appears(selenium, base_url, faker):
    selenium.get(f'{base_url}/login')
    page = LoginPage(selenium)
    page.login(faker.user_name(), faker.password())

    assert 'Your username is invalid!' in page.flash.get_text()


@pytest.mark.wip
@pytest.mark.nondestructive
def test_if_correct_credentials_are_provided_then_success_message_appears(selenium, base_url, variables):
    selenium.get(f'{base_url}/login')
    page = LoginPage(selenium)
    page.login(variables['heroku']['username'], variables['heroku']['password'])

    assert 'You logged into a secure area!' in page.flash.get_text()
