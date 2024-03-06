from selenium import webdriver
from selenium.webdriver.common.by import By
import os
import openpyxl

def read_credentials_from_excel(file_path):
    credentials =[]
    workbook = openpyxl.load_workbook(file_path)
    sheet = workbook.active


    for row in sheet.iter_rows(min_row=2, values_only=True):
        username,password = row
        credentials.append({"username":username,"password": password})
    return credentials



def test_vwo():
    file_path = os.getcwd()
    #print(file_path)
    full_path = file_path+"/testdata_ddt.xlsx"

    credentials = read_credentials_from_excel(full_path)

    for user_cred in credentials:
        username = user_cred["username"]
        password = user_cred["password"]
        print(username,password)
        vwo_login(username,password)

def vwo_login(username,password):
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://app.vwo.com/#/login")
    driver.find_element(By.CSS_SELECTOR, "#login-username").send_keys(username)
    driver.find_element(By.CSS_SELECTOR, "[name='password']").send_keys(password)
    driver.find_element(By.CSS_SELECTOR, "#js-login-btn").click()
    print(driver.find_element(By.XPATH,"//div[@class='notification-box-description']").text)
    driver.quit()


