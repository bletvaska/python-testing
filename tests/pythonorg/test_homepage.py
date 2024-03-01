import pytest
from selenium.webdriver.common.by import By


@pytest.fixture()
def homepage(browser):
    browser.get('https://www.python.org')
    yield browser


def test_failing_test(homepage):
    assert False, 'This will always fail'


def test_when_search_string_entered_then_results_must_show_on_page(homepage):
    # act
    element = homepage.find_element(By.ID, 'id-search-field')
    element.send_keys('pycon')
    element.submit()

    # assert
    homepage.find_element(By.TAG_NAME, 'h2')


def test_when_on_homepage_then_python_in_title(homepage):
    # assert
    assert 'Python' in homepage.title, 'No Python in title.'


def test_when_on_homepage_then_searchbar_is_present(homepage):
    # act / assert
    homepage.find_element(By.ID, 'id-search-field')
