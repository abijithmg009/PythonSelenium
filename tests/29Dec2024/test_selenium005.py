import time

from selenium import webdriver

# Chrome -> # Chrome Options
# Edge -> Edge Options
# Firefox -> Firefox Options

def test_open_login():
    driver = webdriver.Chrome()
    driver.get("https://google.com")
    #driver.navigate(). will not work in Python but work on Java
    print(driver.title)
    driver.refresh()
    driver.get("https://www.bing.com")
    print(driver.title)
    driver.back()
    driver.refresh()
    time.sleep(5)
    driver.quit()