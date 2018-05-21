import unittest
from selenium import webdriver
from selenium.webdriver.support.select import Select


class JobTitleSearch(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome('/home/eduard/Selenium_HRM_Spring2018/chromedriver')
        self.driver.maximize_window()
        # Optional argument, if not specified will search path.
        url = 'http://hrm.seleniumminutes.com'
        self.driver.get(url)


    def test_job_title(self):
        driver = self.driver
        driver.find_element_by_id('txtUsername').send_keys('admin')
        driver.find_element_by_id('txtPassword').send_keys('Password')
        driver.find_element_by_id('btnLogin').click()
        driver.find_element_by_id('menu_pim_viewPimModule').click()
        select = Select(driver.find_element_by_id('empsearch_job_title'))
        # select.select_by_visible_text('QA Manager')
        select.select_by_value('2')
        table = driver.find_element_by_id('resultTable')
        print(table[1])



if __name__ == '__main__':
    unittest.main()
