import time
from selenium import webdriver
from selenium.webdriver.common.by import By


def test_ebay():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://app.vwo.com/#/login")
    driver.find_element(By.CSS_SELECTOR, "#login-username").send_keys("contact+atb5x@thetestingaccademy.com")
    time.sleep(5)