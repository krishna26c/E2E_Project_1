from selenium import webdriver
from Base.Initiate_browser import startBrower, CloseDriver
import time
global driver, browser

def test_openbrower():
    driver = startBrower()
    driver.maximize_window()

