from selenium import webdriver
from selenium.webdriver.common.by import By


def test_when_on_homepage_then_python_in_title():
    # arrange
    driver = webdriver.Chrome()
    driver.get('https://www.python.org')

    # assert
    assert 'Python' in driver.title, 'No Python in title.'

    driver.close()


def test_when_on_homepage_then_searchbar_is_present():
    # arrange
    driver = webdriver.Chrome()
    driver.get('https://www.python.org')

    # act / assert
    driver.find_element(By.ID, 'id-search-field')

    driver.close()


def test_when_search_string_entered_then_results_must_show_on_page():
    # arrange
    driver = webdriver.Chrome()
    driver.get('https://www.python.org')

    # act
    element = driver.find_element(By.ID, 'id-search-field')
    element.send_keys('pycon')
    element.submit()

    # assert
    driver.find_element(By.TAG_NAME, 'h2')

    driver.close()
