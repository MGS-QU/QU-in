import time

import XLUtils
from selenium import webdriver

driver = webdriver.Chrome(executable_path="C:\\chromedriver.exe")

driver.get("https://test.queueyu.com/login")
driver.maximize_window()
driver.find_element_by_link_text("Don't have an account? Sign Up").click()

path = "C://Users/DELL-PC/PycharmProjects1/Qu-in PWA/Data Driven//DataDrivenSignUp.xlsx"

rows = XLUtils.getRowCount(path,"SignUp")

for r in range(2,rows+1):
    Email = XLUtils.readData(path, 'SignUp', r, 1)
    CountryCode = XLUtils.readData(path, 'SignUp', r, 2)
    PhoneNumber = XLUtils.readData(path, 'SignUp', r, 3)
    Password = XLUtils.readData(path, 'SignUp', r, 4)
    driver.find_element_by_xpath("//input[@id ='outlined-select-currency']").send_keys(Email)
    driver.find_element_by_xpath("//input[@id='combo-box-demo']").send_keys(CountryCode)
    driver.find_element_by_id("phoneNumber").send_keys(PhoneNumber)
    driver.find_element_by_name("password").send_keys(Password)
    driver.find_element_by_xpath("//span[@class='MuiButton-label']").click()
    if driver.title == "QU WEB CLIENT/Login":
        time.sleep(10)
        print("Account already Exists")
        XLUtils.writeData(path, 'SignUp', r, 5, "Failed ")
    else:
        driver.get("https://test.queueyu.com/login")
        driver.maximize_window()
        driver.find_element_by_link_text("Don't have an account? Sign Up").click()
        time.sleep(15)
        driver.find_element_by_xpath("//span[@class='MuiButton-label']").click()
        XLUtils.writeData(path, 'SignUp', r, 5, "Pass")


driver.quit()



