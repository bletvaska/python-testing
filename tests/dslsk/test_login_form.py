import pytest
from selenium.webdriver.common.by import By

pytestmark = [
    pytest.mark.heroku,
    pytest.mark.login_form,
    pytest.mark.nondestructive
]


@pytest.mark.wip
def test_when_correct_credentials_are_provided_then_redirected_to_secure_page(selenium, base_url):
    selenium.get(f'{base_url}/login')
    selenium.find_element(By.ID, 'username').send_keys('tomsmith')
    selenium.find_element(By.ID, 'password').send_keys('SuperSecretPassword!')
    selenium.find_element(By.TAG_NAME, 'button').click()
    element = selenium.find_element(By.ID, 'flash')
    assert selenium.current_url == f'{base_url}/secure'


@pytest.mark.repeat(10)
def test_when_only_login_is_submitted_then_error_message_is_displayed(selenium, faker, base_url):
    selenium.get(f'{base_url}/login')
    selenium.find_element(By.ID, 'username').send_keys(faker.user_name())
    selenium.find_element(By.TAG_NAME, 'button').click()
    element = selenium.find_element(By.ID, 'flash')
    assert 'Your username is invalid!' in element.text


def test_when_empty_form_is_submitted_then_error_message_is_displayed(selenium, base_url):
    # arrange
    selenium.get(f'{base_url}/login')

    # act
    selenium.find_element(By.TAG_NAME, 'button').click()

    # assert
    element = selenium.find_element(By.ID, 'flash')
    assert 'Your username is invalid!' in element.text
