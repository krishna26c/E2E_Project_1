from selenium import webdriver
global driver
from Library import ConfigReader

def start_browser():
    browser=ConfigReader.readconfigData("Details", "Browser")
    print(browser)
    if browser=="Chrome":
        driver=webdriver.Chrome(executable_path="chromedriver.exe")
    elif browser=="Firefox":
        driver = webdriver.Firefox(executable_path="geckodriver.exe")

    driver.get(ConfigReader.readconfigData("Details", "Application_url"))
    driver.maximize_window()
    return driver
def close_browser():
    driver.close_window()