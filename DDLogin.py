import time
import XLUtils
from selenium import webdriver

driver = webdriver.Chrome(executable_path="C:\\chromedriver.exe")

driver.get("https://test.queueyu.com/login")
driver.maximize_window()

path = "C://Users/DELL-PC/PycharmProjects1/Qu-in PWA/Data Driven/DataDrivenLogin.xlsx"

rows = XLUtils.getRowCount(path,'Login')

for r in range(2, rows+1):
    Username = XLUtils.readData(path, 'Login', r, 1)
    Password = XLUtils.readData(path, 'Login', r, 2)

    driver.find_element_by_id("email id").send_keys(Username)
    driver.find_element_by_id("password").send_keys(Password)

    driver.find_element_by_xpath("//span[text()='Login']").click()
    time.sleep(5)

    if driver.title == "QU WEB CLIENT":
        print("Test is Passed")
        XLUtils.writeData(path, 'Login', r, 3,"Pass")

    else:
        print("Test is failed")
        XLUtils.writeData(path, 'Login', r, 3, "Fail")

driver.find_element_by_xpath("//header/div[1]/div[1]/div[3]/button[1]").click()
driver.find_element_by_xpath("//span[contains(text(),'Logout')]").click()
driver.find_element_by_xpath("//span[contains(text(),'Yes')]").click()
