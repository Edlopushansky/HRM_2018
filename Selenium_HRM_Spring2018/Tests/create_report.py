import unittest
import random

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

from common.common import login, get_welcome_message


class CreateReport(unittest.TestCase):
    def setUp(self):
        url = 'http://hrm.seleniumminutes.com'
        self.driver = webdriver.Chrome('/home/eduard/Selenium_HRM_Spring2018/chromedriver')
        self.driver.maximize_window()

        self.driver.get(url)
        self.wait = WebDriverWait(self.driver, 25)

    def test_create_report(self):
        driver = self.driver

        login(driver)

        self.assertEqual('Welcome Admin', get_welcome_message(driver))

        driver.find_element_by_id('menu_pim_viewPimModule').click()
        driver.find_element_by_id('menu_core_viewDefinedPredefinedReports').click()

        driver.find_element_by_id('btnAdd').click()

        report_name = 'Report' + str(random.randint(100000,999999))

        driver.find_element_by_id('report_report_name').send_keys(report_name)
        Select(driver.find_element_by_id('report_criteria_list')).select_by_visible_text('Job Title')
        driver.find_element_by_id('btnAddConstraint').click()

        Select(driver.find_element_by_id('report_display_groups')).select_by_visible_text('Personal ')
        driver.find_element_by_id('btnAddDisplayGroup').click()
        self.wait.until(EC.visibility_of_element_located((By.ID, 'display_group_1'))).click()
        driver.find_element_by_id('btnSave').click()

        self.assertTrue(self.driver.find_element_by_css_selector('.message.success'), 'Successfully Saved')

        #search to report
        driver.find_element_by_id('search_search').send_keys(report_name)
        driver.find_element_by_name('_search').click()

        #assert report exists
        self.assertTrue(report_name, driver.find_element_by_xpath('//td[2]').text)

        #run report
        driver.find_element_by_xpath('//td[3]/a').click()

        self.assertTrue(len(driver.find_elements_by_xpath('//tbody/tr')) >= 1)

        driver.find_element_by_id('menu_pim_viewPimModule').click()
        driver.find_element_by_xpath('//li/a[text()= "Reports"]').click()
        driver.find_element_by_id('search_search').send_keys(report_name)
        driver.find_element_by_name('_search').click()

    def tearDown(self):
        self.driver.find_element_by_xpath('//input[contains(@id,"ohrmList_chkSelectRecord")]').click()
        self.driver.find_element_by_id('btnDelete').click()

        self.driver.find_element_by_css_selector('input#dialogDeleteBtn').click()
        self.assertTrue(self.driver.find_element_by_css_selector('.message.success'), 'Successfully Deleted')


if __name__ == '__main__':
    unittest.main()
