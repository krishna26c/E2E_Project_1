from selenium import webdriver
global driver

def startBrower():
    driver = webdriver.Chrome(executable_path="C:\\Users\91807\PycharmProjects\E2E_Project\chromedriver.exe")
    driver.get("http://magento-demo.lexiconn.com/customer/account/create/")
    return driver

def CloseDriver():
    driver.close()
    return driver