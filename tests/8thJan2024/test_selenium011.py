import time
from selenium import webdriver
from selenium.webdriver.common.by import By


def test_ebay():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://www.ebay.com/")
    driver.find_element(By.XPATH, "//input[@type='text']").send_keys("16gb laptop")
    driver.find_element(By.XPATH,"//input[@type='submit']").click()
    time.sleep(5) # we will remove this

    list_result = driver.find_elements(By.XPATH,"//span[@role='heading']")
    for i in list_result:
        if i.text == "NEW LISTINGDell Inspiron 15 5505 256GB SSD 16Gb Ram Integrated Vega Graphics":
            



