from selenium import webdriver


def test_when_on_homepage_then_python_in_title():
    # arrange
    driver = webdriver.Chrome()
    driver.get('https://www.python.org')

    # assert
    assert 'Python' in driver.title, 'No Python in title.'

    driver.close()
