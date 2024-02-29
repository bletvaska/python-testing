import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By


@pytest.fixture
def browser():
    driver = webdriver.Chrome()
    driver.get('https://www.python.org')

    yield driver

    driver.close()


def test_when_on_homepage_then_python_in_title(browser):
    # assert
    assert 'Python' in browser.title, 'No Python in title.'


def test_when_on_homepage_then_searchbar_is_present(browser):
    # act / assert
    browser.find_element(By.ID, 'id-search-field')


def test_when_search_string_entered_then_results_must_show_on_page(browser):
    # act
    element = browser.find_element(By.ID, 'id-search-field')
    element.send_keys('pycon')
    element.submit()

    # assert
    browser.find_element(By.TAG_NAME, 'h2')
