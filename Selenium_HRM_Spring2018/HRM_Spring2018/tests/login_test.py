import unittest
from time import sleep
from unittest import skip

from selenium import webdriver
from steps.common import get_welcome_message

# Test Case class starts here
class MyTestCase(unittest.TestCase):

    # setUp will get executes by unittest once for every function which starts with 'test'
    def setUp(self):
        self.driver = webdriver.Chrome(executable_path='/Users/ellie/Selenium/HRM_Spring2018/browser_drivers/chromedriver')
        self.driver.get('http://hrm-online.portnov.com')

    # it is also wise to add a tearDown() function - we will do this next class

    def test_valid_login(self):
        driver = self.driver
        driver.find_element_by_id('txtUsername').send_keys('admin')
        driver.find_element_by_id('txtPassword').send_keys('password')
        driver.find_element_by_id('btnLogin').click()

        welcome_text = get_welcome_message(driver)

        # Expected value vs. Actual value
        self.assertEqual('Welcome Admin', welcome_text)

    def test_invalid_password(self):
        driver = self.driver
        driver.find_element_by_id('txtUsername').send_keys('admin')
        driver.find_element_by_id('txtPassword').send_keys('PASS123')
        driver.find_element_by_id('btnLogin').click()

        sleep(2)

        warning_text = driver.find_element_by_id('spanMessage').text

        # Expected value vs. Actual value
        self.assertEqual('Invalid credentials', warning_text)

    def test_empty_password(self):
        driver = self.driver
        driver.find_element_by_id('txtUsername').send_keys('admin')
        driver.find_element_by_id('btnLogin').click()

        sleep(2)

        warning_text = driver.find_element_by_id('spanMessage').text

        # Expected value vs. Actual value
        self.assertEqual('Password cannot be empty', warning_text)

# Test Case class ends here


if __name__ == '__main__':
    unittest.main()
