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
    #driver.find_element(By.PARTIAL_LINK_TEXT,"Make Appointment").click()
    #driver.find_element(By.CLASS_NAME,("btn.btn-dark.btn-lg")[1]).click() there are 3 same values so better don't use


    time.sleep(5)


