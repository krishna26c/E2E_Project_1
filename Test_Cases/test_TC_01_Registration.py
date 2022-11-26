from selenium.webdriver.common.by import By
from Base import Initiate_browser
from Library import ConfigReader

def test_Registration():
    print("\nTest Registration called")
    driver=Initiate_browser.start_browser()
    driver.find_element(By.XPATH, ConfigReader.fetchelement("Registration", "username")).send_keys("Samrata@gmail.com")
    driver.find_element(By.XPATH, ConfigReader.fetchelement("Registration", "password")).send_keys("samrata@123")
    driver.find_element(By.XPATH, ConfigReader.fetchelement("Registration", "button")).click()
    msg=driver.find_element(By.XPATH, ConfigReader.fetchelement("WelcomePage", "welcomeText")).text
    assert 'SAMRATA' in msg, "User not valid"

