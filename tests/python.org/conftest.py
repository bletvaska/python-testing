import pytest
from selenium import webdriver


@pytest.fixture(scope="module")
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()


@pytest.fixture(scope="session")
def base_url():
    yield "https://www.python.org"
