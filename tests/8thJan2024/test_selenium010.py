import time
import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By


def test_login():
    driver = webdriver.Chrome()
    driver.get("https://awesomeqa.com/xpath/")

    assert driver.current_url == "https://awesomeqa.com/xpath/"

    #/ancestor,descendant,
    ancestor_of_mammal = driver.find_element(By.XPATH, "//div[@class ='Mammal']/ancestor::div")
    print(ancestor_of_mammal.text)