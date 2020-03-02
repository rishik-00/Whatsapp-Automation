import unittest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
import time

class LoginTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(executable_path = 'C:\\Users\\Rishik\\Downloads\\chromedriver_win32\\chromedriver.exe')
        self.driver.get("https://www.facebook.com")
        self.driver.maximize_window()


    def test_login(self):
        driver = self.driver
        username = #enter your username
        password = #enter your password

        emailid = 'email'
        passid = 'pass'
        loginbuttonxpath = '//input[@value = "Log In"]'
        fblogoXpath = '(//a[contains(@href,"logo")])[1]'

        emailelement = WebDriverWait(driver,10).until(lambda driver : driver.find_element_by_id(emailid))
        passelement =  WebDriverWait(driver,10).until(lambda driver : driver.find_element_by_id(passid))
        loginbuttonelement = WebDriverWait(driver,10).until(lambda driver : driver.find_element_by_xpath(loginbuttonxpath))

        emailelement.clear()
        emailelement.send_keys(username)
        passelement.clear()
        passelement.send_keys(password)
        loginbuttonelement.click()
        WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_xpath(fblogoXpath))

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()