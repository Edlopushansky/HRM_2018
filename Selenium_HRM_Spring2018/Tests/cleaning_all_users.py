##############################################
##############################################
from selenium import webdriver
import unittest

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from common.common import login


class CleanAllUsers(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome('/home/eduard/Selenium_HRM_Spring2018/chromedriver')
        self.driver.maximize_window()
        url = 'http://hrm.seleniumminutes.com'
        self.driver.get(url)
        self.wait = WebDriverWait(self.driver,25)

    def test_cleanup(self):
        driver = self.driver

        login(driver)
        driver.find_element_by_id('menu_pim_viewPimModule').click()

        number_of_elements = driver.find_elements_by_xpath('//tbody/tr').count()

        while number_of_elements <= int(driver.find_element_by_class_name('desc').text[-1]):
            driver.find_element_by_id('ohrmList_chkSelectAll').click()
            driver.find_element_by_id('btnDelete').click()

    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
