import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By


# Chrome -> # Chrome Options
# Edge -> Edge Options
# Firefox -> Firefox Options

def test_open_login():
    driver = webdriver.Firefox()
    driver.get("https://relc.dev.playosmo.com")
    driver.maximize_window()
    #driver.navigate(). will not work in Python but work on Java
    print(driver.title)
    driver.refresh()
    driver.quit()
