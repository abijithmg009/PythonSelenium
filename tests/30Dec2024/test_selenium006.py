#Open the browser
# Navigate to the URL
#Find the email web element, and enter the email address
#Find the password input box, and the password
#click on signin button
import time

#Verify the dashboard is loaded - Pytest
#Create a report and send to QA lead - HTML or allure report


from selenium import webdriver
import pytest
from selenium.webdriver.common.by import By
import logging


def test_vwologin():
    LOGGER = logging.getLogger(__name__)
    driver = webdriver.Chrome()
    chromeoptions = webdriver.ChromeOptions()
    chromeoptions.add_argument("--start-maximize")
    time.sleep(5)
    driver.get("https://app.vwo.com")
    '''
    type, class, name, id and one custom attribute
        <input type="email" class="text-input W(100%)" name="username" id="login-username" data-qa="hocewoqisi">
    
    selenium provide different ways to find elements on webpage
    find_element by_id : finding an element by it's unique id attribute
    find_element by_name : find an element by it's name attribute
    find_element by_xplath : find an element using an XPath expression
    find_element by_link_text : finds an anchor element (a) by it's visible text
    find_element by_partial_link_text : finds an anchor element (a) by a partial match of it's link
    find_element by_tag_name : finds an element by it's HTML tag name (eg:div, "input"
    find_element by_class_name : find an element by it's css class name 
    '''
    email_address_ele = driver.find_element(By.ID,"login-username")
    password_ele = driver.find_element(By.NAME,"password")
    signin_button_ele =  driver.find_element(By.ID, "js-login-btn")
    '''
    sending the data and click functions
    '''
    email_address_ele.send_keys("contact+atb5x@thetestingacademy.com")
    password_ele.send_keys("ATBx@1234")
    signin_button_ele.click()
    #There is a delay of 2-3 seconds to
    time.sleep(5)
    LOGGER.info("Title is "+driver.title)
    assert "Dashboard" in driver.title

    driver.refresh()
    driver.get("https://www.google.com")
    LOGGER.warning("New title is "+driver.title)
    driver.back()
    driver.refresh()
    driver.forward()



