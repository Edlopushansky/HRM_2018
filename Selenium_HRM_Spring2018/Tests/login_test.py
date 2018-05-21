
#


import time
import unittest
from selenium import webdriver


class LoginPage(unittest.TestCase):


    def setUp(self):
        self.driver = webdriver.Chrome('/home/eduard/Selenium_HRM_Spring2018/chromedriver')
        self.driver.maximize_window()
        # Optional argument, if not specified will search path.
        url = 'http://hrm-online.portnov.com'
        self.driver.get(url)

    def test_valid_login(self):
        driver = self.driver
        driver.find_element_by_id('txtUsername').send_keys('admin')
        driver.find_element_by_id('txtPassword').send_keys('password')
        driver.find_element_by_id('btnLogin').click()

        welcome_text = driver.find_element_by_id('welcome').text
        self.assertEqual('Welcome Admin', welcome_text)

    def test_invalid_login(self):
        driver = self.driver
        driver.find_element_by_id('txtUsername').send_keys('admin')
        driver.find_element_by_id('txtPassword').send_keys('Password')

        driver.find_element_by_id('btnLogin').click()

        warning_message = driver.find_element_by_id('spanMessage').text

        self.assertEqual('Invalid credentials', warning_message)

    def test_no_password(self):
        driver = self.driver
        driver.find_element_by_id('txtUsername').send_keys('admin')
        driver.find_element_by_id('btnLogin').click()

        error_message = driver.find_element_by_id('spanMessage').text
        self.assertEqual(error_message,'Password cannot be empty')


    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()