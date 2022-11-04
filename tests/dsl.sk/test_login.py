import pytest
from selenium.webdriver.common.by import By


@pytest.mark.skip
def test_if_correct_login_and_passwords_are_entered_then_current_url_will_be_dsl(driver):
    # arrange
    username = driver.find_element(By.XPATH, '//input[@name="login"]')
    password = driver.find_element(By.XPATH, '//input[@name="password"]')
    button = driver.find_element(By.XPATH, '//*[@id="body"]/table/tbody/tr/td/form/input[7]')

    # act
    username.send_keys("pytester")
    password.send_keys("pytester")
    button.click()

    # assert
    assert driver.current_url == "https://www.dsl.sk/"

    driver.get("https://www.dsl.sk/user.php?action=logout")


def test_if_empty_form_is_submitted_then_current_url_will_be_same(driver):
    # arrange
    button = driver.find_element(By.XPATH, '//*[@id="body"]/table/tbody/tr/td/form/input[7]')

    # act
    button.click()

    # assert
    assert driver.current_url == "https://www.dsl.sk/user.php"


def test_if_empty_form_is_submitted_then_info_message_should_appear(driver):
    # arrange
    button = driver.find_element(By.XPATH, '//*[@id="body"]/table/tbody/tr/td/form/input[7]')

    # act
    button.click()
    message = driver.find_element(By.XPATH, '//*[@id="body"]/table/tbody/tr/td/form/b')

    # assert
    message = driver.find_element(By.XPATH, '//*[@id="body"]/table/tbody/tr/td/form/b')
    assert message.text == "Nesprávne meno alebo heslo alebo Váš email nebol zatiaľ overený."


def test_when_login_is_entered_and_no_password_then_remain_on_same_url(driver, faker):
    # arrange
    username = driver.find_element(By.XPATH, '//input[@name="login"]')
    username.send_keys(faker.user_name())

    # act
    button = driver.find_element(By.XPATH, '//*[@id="body"]/table/tbody/tr/td/form/input[7]')
    button.click()

    # assert
    assert driver.current_url == "https://www.dsl.sk/user.php"


def test_when_login_and_invalid_password_are_entered_then_remain_on_same_url(driver, faker):
    # arrange
    username = driver.find_element(By.XPATH, '//input[@name="login"]')
    username.send_keys(faker.user_name())
    password = driver.find_element(By.XPATH, '//input[@name="password"]')
    password.send_keys(faker.password())

    # act
    button = driver.find_element(By.XPATH, '//*[@id="body"]/table/tbody/tr/td/form/input[7]')
    button.click()

    # assert
    assert driver.current_url == "https://www.dsl.sk/user.php"


def test_if_correct_login_name_with_empty_password_is_submitted_then_show_wrong_password_account_not_verified(driver):
    # arrange
    username = driver.find_element(By.XPATH, '//input[@name="login"]')
    password = driver.find_element(By.XPATH, '//input[@name="password"]')
    button = driver.find_element(By.XPATH, '//*[@id="body"]/table/tbody/tr/td/form/input[7]')

    # act
    username.send_keys("pytester")
    password.send_keys("")
    button.click()

    # assert
    # <b>Nesprávne meno alebo heslo alebo Váš email nebol zatiaľ overený.</b>
    assert driver.find_element(By.XPATH, '//*[@id="body"]/table/tbody/tr/td/form/b')


def test_if_correct_login_name_with_wrong_password_is_submitted_then_show_wrong_password_account_not_verified(
    driver, faker
):
    # arrange
    username = driver.find_element(By.XPATH, '//input[@name="login"]')
    password = driver.find_element(By.XPATH, '//input[@name="password"]')
    button = driver.find_element(By.XPATH, '//*[@id="body"]/table/tbody/tr/td/form/input[7]')

    # act
    username.send_keys("pytester")
    password.send_keys(faker.password())
    button.click()

    # assert
    # <b>Nesprávne meno alebo heslo alebo Váš email nebol zatiaľ overený.</b>
    assert driver.find_element(By.XPATH, '//*[@id="body"]/table/tbody/tr/td/form/b')
