import time

from selenium import webdriver
from selenium.webdriver.common.by import By


def test_login():
    driver = webdriver.Chrome()
    driver.get("https://katalon-demo-cura.herokuapp.com/")
    assert driver.title == "CURA Healthcare Service"

    #//tagname[@attribute=value]
    driver.find_element(By.XPATH, "//a[@id='btn-make-appointment']").click()
    assert driver.title == "CURA Healthcare Service"
    assert driver.current_url == "https://katalon-demo-cura.herokuapp.com/profile.php#login"
    #Xpath functions:
    #Contains - //a[contains(text(),'Make')], It will basically helps to match the text partially.
                # //tag_name[containts(@attribute,'value')]
    # we can use and or not as well,  //p[contains(text(),'A') and contains(@classname,'muted')]
    #text() - //a[text()='Make Appointment'] - Full visible text.
    #Start-with
    #Ends-with





    time.sleep(5)
    driver.quit()
