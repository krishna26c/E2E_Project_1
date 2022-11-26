from selenium import webdriver
from selenium.webdriver.common.by import By
from Base.Initiate_browser import start_browser
import time
global driver, browser
from Library import ConfigReader

def test_openbrower():
    driver = start_browser()
    driver.maximize_window()
    driver.find_element(By.XPATH, ConfigReader.fetchelement("Registration", "username")).send_keys("scb201@gmail.com")
    driver.find_element(By.XPATH, ConfigReader.fetchelement("Registration", "password")).send_keys("scb_pass")
    driver.find_element(By.XPATH, ConfigReader.fetchelement("Registration", "button")).click()






