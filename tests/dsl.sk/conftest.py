import pytest
from selenium import webdriver


@pytest.fixture(scope="module")
def driver(base_url):
    options = webdriver.ChromeOptions()
    options.add_argument('headless')

    # setup
    driver = webdriver.Chrome(options=options)
    driver.get(base_url)

    yield driver

    # teardown
    driver.quit()


@pytest.fixture(scope="session")
def base_url():
    yield "https://www.dsl.sk/user.php?action=login"
