from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest


@pytest.mark.wip
def test_when_url_is_opened_then_python_should_be_in_title():
    driver = webdriver.Chrome()
    driver.get('https://www.python.org')
    assert 'Python' in driver.title
