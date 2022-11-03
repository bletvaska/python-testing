from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest


@pytest.fixture(scope="module")
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()


def test_when_url_is_opened_then_python_should_be_in_title(driver):
    # arrange / act
    driver.get("https://www.python.org")

    # assert
    assert "Python" in driver.title


def test_when_string_is_searched_then_results_must_be_labeled_in_h3(faker, driver):
    # arrange
    driver.get("https://www.python.org")

    # act
    # search for search bar
    element = driver.find_element(By.NAME, "q")
    element.send_keys(faker.sentence())
    element.submit()

    # assert
    element = driver.find_element(By.TAG_NAME, "h3")
    assert element.text == "Results"
