import pytest
from selenium import webdriver


@pytest.fixture(scope='module')
def browser():
    # setup
    options = webdriver.ChromeOptions()
    options.add_argument('headless')
    driver = webdriver.Chrome(options=options)
    driver.get('http://www.python.org')

    yield driver

    # teardown
    driver.close()


def test_when_page_is_loaded_then_python_should_be_in_title(browser):
    assert 'Python' in browser.title


def test_when_pycon_is_searched_then_results_are_shown(browser):
    elem = browser.find_element_by_id('id-search-field')
    elem.send_keys('pycon\n')
    h3 = browser.find_element_by_xpath('//*[@id="content"]/div/section/form/h3')
    assert 'Results' in h3.text
