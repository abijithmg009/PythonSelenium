#selenium 4  has W3C protocol, there is selenium manager which will automatically download the
#browser driver
import time

import pytest
from selenium import webdriver
import logging

@pytest.fixture()
def driver():

    driver = webdriver.Chrome()
    yield driver  # gives less memory ad we are not storing
    # return WebDriver #values will be stored  and extra variable is created


def test_open_url_verify_title(driver):
    chromeoptions = webdriver.ChromeOptions()
    extension_path = "/Users/abijithmg/Downloads/ad blocker.crx"
    chromeoptions.add_extension(extension_path)
    chromeoptions.add_argument("--start-maximized")
    driver = webdriver.Chrome(chromeoptions)
    LOGGER = logging.getLogger(__name__)
    driver.get("https://www.google.com")
    driver.maximize_window()
    LOGGER.info(driver.title)
    #verification
    assert "Google" == driver.title, "Expected"
    driver.quit()