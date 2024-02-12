import time

import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By


def test_login():
    driver = webdriver.Chrome()
    driver.get("https://www.idrive360.com/enterprise/login")
    abs_path = driver.find_element(By.XPATH, "/html/body/app-root/app-login/app-signin/div/section/div/div/form/div[2]/div[1]/fieldset/div[5]/div[1]/input")
    abs_path.send_keys("admin")
    rel_path = driver.find_element(By.XPATH,"//input[@id = 'password']")
    rel_path.send_keys("admin")
    driver.find_element(By.XPATH,"//button[@class='id-btn id-info-btn-frm']").click()
    time.sleep(5)