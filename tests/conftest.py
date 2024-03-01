import pytest
from faker import Faker
from selenium import webdriver


@pytest.fixture(scope='module')
def browser():
    options = webdriver.ChromeOptions()
    # options.add_argument('headless')
    driver = webdriver.Chrome(options=options)

    # options = webdriver.FirefoxOptions()
    # options.add_argument('--headless')
    # driver = webdriver.Firefox(options=options)

    yield driver

    driver.close()


@pytest.fixture(scope='session')
def faker():
    yield Faker()
