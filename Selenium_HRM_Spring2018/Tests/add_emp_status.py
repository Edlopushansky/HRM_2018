import random
import unittest
# from random import randint
# from time import sleep

from selenium import webdriver
from faker import Faker
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

from common.common import get_welcome_message


class AddEmployee(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome('/home/eduard/Selenium_HRM_Spring2018/chromedriver')
        self.driver.maximize_window()
        # url = 'http://hrm-online.portnov.com'
        url = 'http://hrm.seleniumminutes.com'
        self.driver.get(url)
        self.wait = WebDriverWait(self.driver, 25)


    def test_add_employee(self):

        """"
        login
        click to Add button
        enter First and Last name
        enter and remember the empId
        save the employee
        go to PIM page
        search  by empId
        expected: 1 record back
        expected correct name and empID
        """
        empId = random.randint(100000, 9999999)
        fake = Faker()
        first_name = fake.first_name()
        last_name = fake.last_name()
        expected_job_title = 'QA Manager'
        expected_job_status = 'Full-time'

        driver = self.driver
        driver.find_element_by_id('txtUsername').send_keys('admin')
        driver.find_element_by_id('txtPassword').send_keys('Password')
        driver.find_element_by_id('btnLogin').click()

        welcome_text = get_welcome_message(driver)

        self.assertEqual('Welcome Admin', welcome_text)

        driver.find_element_by_id('menu_pim_viewPimModule').click()
        driver.find_element_by_id('btnAdd').click()
        driver.find_element_by_id('firstName').send_keys(first_name)
        driver.find_element_by_id('lastName').send_keys(last_name)
        driver.find_element_by_id('employeeId').clear()
        driver.find_element_by_id('employeeId').send_keys(empId)
        driver.find_element_by_id('btnSave').click()

        driver.find_element_by_xpath('//*[@id="sidenav"]/li[6]/a').click()
        # driver.find_element_by_link_text('Job').click()
        driver.find_element_by_id('btnSave').click()
        driver.find_element(By.TAG_NAME,'iframe')

        Select(driver.find_element_by_id('job_job_title')).select_by_visible_text(expected_job_title)
        Select(driver.find_element_by_id('job_emp_status')).select_by_visible_text(expected_job_status)

        driver.find_element_by_id('btnSave').click()
        locator = (By.CSS_SELECTOR, '.message.success')
        self.wait.until(expected_conditions.presence_of_element_located(locator))


        driver.find_element_by_id('menu_pim_viewPimModule').click()
        driver.find_element_by_id('empsearch_id').send_keys(empId)
        driver.find_element_by_id('searchBtn').click()

        #Expected: 1 record back
        # self.assertTrue(len(driver.find_elements_by_xpath('//td[3]/a' ))== 1)

        #expected correct name and empID
        firstName = driver.find_element_by_xpath('//td[3]/a').text
        lastName = driver.find_element_by_xpath('//td[4]/a').text
        employeeId = driver.find_element_by_xpath('//td[2]/a').text
        job_title = driver.find_element_by_xpath('//td[5]').text
        emp_status = driver.find_element_by_xpath('//td[6]').text

        self.assertEqual(first_name,firstName)
        self.assertEqual(last_name,lastName)
        self.assertEqual(empId,int(employeeId))
        self.assertEqual(job_title,expected_job_title)
        self.assertEqual(emp_status, expected_job_status)

    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
