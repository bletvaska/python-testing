import pytest
from selenium.webdriver.common.by import By

pytestmark = [
    pytest.mark.dslsk,
    pytest.mark.login_form
]


@pytest.fixture
def login_page(browser):
    browser.get('https://www.dsl.sk/user.php?action=login')
    yield browser


# ak zadam spravny login a spravne heslo tak ma presmeruje na stranku https://www.dsl.sk/ .
def test_if_valid_login_and_password_entered_then_user_is_logged_in(login_page, config):
    # arrange
    username = login_page.find_element(By.NAME, 'login')
    username.send_keys(config['username'])
    password = login_page.find_element(By.NAME, 'password')
    password.send_keys(config['password'])

    # act
    button_xpath = '/html/body/table/tbody/tr/td/div/table/tbody/tr[1]/td[2]/div/table/tbody/tr/td/form/input[7]'
    login_page.find_element(By.XPATH, button_xpath).click()

    # assert
    # assert login_page.current_url == 'https://www.dsl.sk/'
    element = login_page.find_element(By.XPATH, '/html/body/table/tbody/tr/td[1]/div/div[2]/table/tbody/tr/td[1]')
    assert f'prihlásený: {config["username"]}' in element.text

    # cleanup
    login_page.get('https://www.dsl.sk/user.php?action=logout')


@pytest.mark.wip
def test_when_no_password_entered_then_not_logged_in(login_page, config):
    # arrange
    username = login_page.find_element(By.NAME, 'login')
    username.send_keys(config['username'])

    # act
    button_xpath = '/html/body/table/tbody/tr/td/div/table/tbody/tr[1]/td[2]/div/table/tbody/tr/td/form/input[7]'
    login_page.find_element(By.XPATH, button_xpath).click()

    # assert
    element = login_page.find_element(By.XPATH,
                                      '/html/body/table/tbody/tr/td/div/table/tbody/tr[1]/td[2]/div/table/tbody/tr/td/form/b')
    assert 'Nesprávne meno alebo heslo alebo Váš email nebol zatiaľ overený.' in element.text
