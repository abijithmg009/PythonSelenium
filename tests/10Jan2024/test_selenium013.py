import time
import os

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import (ElementNotVisibleException,ElementNotSelectableException)
from dotenv import load_dotenv

@pytest.mark.positive
def test_vwo():
    load_dotenv()
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://app.vwo.com/#/login")
    driver.find_element(By.CSS_SELECTOR, "#login-username").send_keys(os.getenv("EMAIL"))
    driver.find_element(By.CSS_SELECTOR,"[name='password']").send_keys(os.getenv("PASSWORD"))
    driver.find_element(By.CSS_SELECTOR,"#js-login-btn").click()

    WebDriverWait(driver,10).until(
        EC.text_to_be_present_in_element((By.CSS_SELECTOR,".page-heading"), "Dashboard")
    )
    heading_text = driver.find_element(By.XPATH,"//span[@data-qa='lufexuloga']")
    assert heading_text.text == os.getenv("USERNAME")

    time.sleep(5)
    driver.quit()

