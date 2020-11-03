import csv
import pymongo
from pymongo import MongoClient
from selenium import webdriver

driver = webdriver.Chrome(executable_path="C:\\chromedriver.exe")
driver.get("https://test.queueyu.com/login")
driver.maximize_window()

