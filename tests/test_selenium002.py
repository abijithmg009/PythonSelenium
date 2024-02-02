import pytest
from selenium import webdriver

@pytest.fixture()
def driver():
    driver = webdriver.Chrome()
    yield driver  # gives less memory ad we are not storing
    # return WebDriver #values will be stored  and extra variable is created


def test_open_url_verify_title(driver):
    driver.get("https://app.vwo.com")
    print(driver.title)
    #verification
    assert "Login - VWO" == driver.title, "Expected"
    driver.close()