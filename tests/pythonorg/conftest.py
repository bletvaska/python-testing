import pytest
from selenium import webdriver


@pytest.fixture(scope='module')
def browser():
    options = webdriver.ChromeOptions()
    options.add_argument('headless')
    driver = webdriver.Chrome(options=options)

    yield driver

    driver.close()
