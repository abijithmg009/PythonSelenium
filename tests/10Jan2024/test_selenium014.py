#test ebay application


import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import (ElementNotVisibleException,ElementNotSelectableException)




def test_ebay_pclist():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://www.ebay.com/")
    driver.find_element(By.XPATH,"//li[@class='vl-flyout-nav__js-tab']//a[contains(text(),'Electronics')]").click()
    driver.find_element(By.XPATH, "//a[text()='Computers, Tablets & Network Hardware']").click()
    driver.find_element(By.XPATH,"(//img[@role='presentation'])[2]").click()

    WebDriverWait(driver,5).until(
        EC.text_to_be_present_in_element((By.CSS_SELECTOR,"span[class='b-pageheader__text']"),"PC Laptops & Netbooks")
    )

    driver.find_element(By.XPATH,"//p[text()='16 GB']").click()

    WebDriverWait(driver,5).until(
        EC.text_to_be_present_in_element((By.XPATH,"//span[@class='b-pageheader__text']"),"16 GB RAM PC Laptops & Netbooks")

    )

    list = driver.find_elements(By.XPATH,"//h3[@class='s-item__title']")

    for i in list:
        print(i.text)





