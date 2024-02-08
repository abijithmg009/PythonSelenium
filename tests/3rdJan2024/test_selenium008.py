import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
import time


def test_bookappoinment():
    driver = webdriver.Chrome()
    driver.get("https://katalon-demo-cura.herokuapp.com/")
    driver.maximize_window()
    #Click on make appoinment button
    driver.find_element(By.ID,"btn-make-appointment").click()
    print(driver.current_url)
    assert driver.current_url == "https://katalon-demo-cura.herokuapp.com/profile.php#login", "Error wrong URL"

    driver.find_element(By.ID,"txt-username").send_keys("John Doe")
    driver.find_element(By.ID,"txt-password").send_keys("ThisIsNotAPassword")
    driver.find_element(By.ID,"btn-login").click()
    print(driver.current_url)
    assert driver.current_url == "https://katalon-demo-cura.herokuapp.com/#appointment", "Error wrong URL"




    time.sleep(5)