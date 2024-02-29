from selenium.webdriver.common.by import By


def test_when_search_string_entered_then_results_must_show_on_page(browser):
    # arrange
    browser.get('https://www.python.org')

    # act
    element = browser.find_element(By.ID, 'id-search-field')
    element.send_keys('pycon')
    element.submit()

    # assert
    browser.find_element(By.TAG_NAME, 'h2')


def test_when_on_homepage_then_python_in_title(browser):
    # arrange
    browser.get('https://www.python.org')

    # assert
    assert 'Python' in browser.title, 'No Python in title.'


def test_when_on_homepage_then_searchbar_is_present(browser):
    # arrange
    browser.get('https://www.python.org')

    # act / assert
    browser.find_element(By.ID, 'id-search-field')
