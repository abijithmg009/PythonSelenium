import time

import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By


def test_login():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://katalon-demo-cura.herokuapp.com/")
    assert driver.title == "CURA Healthcare Service"
    driver.find_element(By.XPATH, "//a[@id='btn-make-appointment']").click()
    assert driver.current_url == "https://katalon-demo-cura.herokuapp.com/profile.php#login"

    time.sleep(5)
    driver.quit()

def test_login_edge():
    driver = webdriver.Edge()
    driver.maximize_window()
    driver.get("https://katalon-demo-cura.herokuapp.com/")
    assert driver.title == "CURA Healthcare Service"
    driver.find_element(By.XPATH, "//a[@id='btn-make-appointment']").click()
    assert driver.current_url == "https://katalon-demo-cura.herokuapp.com/profile.php#login"

    time.sleep(5)
    driver.quit()