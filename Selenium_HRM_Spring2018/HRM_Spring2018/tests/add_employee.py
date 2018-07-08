import unittest
from random import randint
from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

from fixtures.base import AdminLoginTestCase
from steps.common import login, get_welcome_message, logout

# All of this code is no longer necessary because of inheritance from AdminLoginTestCase
#
# class AddEmployee(unittest.TestCase):
#
#     def setUp(self):
#         self.driver = webdriver.Chrome(
#             executable_path='/Users/ellie/Selenium/HRM_Spring2018/browser_drivers/chromedriver'
#         )
#         self.driver.get('http://hrm-online.portnov.com')
#         self.wait = WebDriverWait(self.driver, 25)
#
#     def tearDown(self):
#         self.driver.quit()


class AddEmployee(AdminLoginTestCase):

    def test_add_employee(self):
        empId = randint(100000,999999)
        expected_job_title = "QA Manager"
        expected_employment_status = "Full Time"
        expected_first_name = "James"
        expected_last_name = "Bond"
        username = "jb" + str(empId)

        driver = self.driver

        # this is performed by the setUp within AdminLoginTestCase fixture
        # login(self.driver)

        welcome_text = get_welcome_message(driver)
        self.assertEqual('Welcome Admin', welcome_text)

        # Click the Add button
        driver.find_element_by_id("btnAdd").click()
        # TODO  EY: may need to come back and do 'something'

        # Enter First and Last name
        driver.find_element_by_id("firstName").send_keys(expected_first_name)
        driver.find_element_by_id("lastName").send_keys(expected_last_name)

        # Enter and remember the empId
        driver.find_element_by_id("employeeId").clear()
        driver.find_element_by_id("employeeId").send_keys(empId)

        # click Create Login Details checkbox
        driver.find_element_by_id("chkLogin").click()

        # wait for the fields to be available
        # fill them in
        self.wait.until(expected_conditions.visibility_of_element_located((By.ID, "user_name"))).send_keys(username)
        driver.find_element_by_id("user_password").send_keys('password')
        driver.find_element_by_id("re_password").send_keys('password')

        # Save the Employee
        driver.find_element_by_id("btnSave").click()

        driver.find_element_by_link_text("Job").click()
        # TODO EY: may need sleep
        driver.find_element_by_id("btnSave").click()
        # TODO EY: may need sleep

        Select(driver.find_element_by_id("job_job_title")).select_by_visible_text(expected_job_title)
        Select(driver.find_element_by_id("job_emp_status")).select_by_visible_text(expected_employment_status)

        driver.find_element_by_id("btnSave").click()
        locator = (By.CSS_SELECTOR, ".message.success")
        self.wait.until(expected_conditions.presence_of_element_located(locator))

        # Go to PIM page
        driver.find_element_by_id("menu_pim_viewPimModule").click()
        # TODO  EY: may need to come back and do 'something' here as well :P

        # Search by EmpId
        driver.find_element_by_id("empsearch_id").send_keys(empId)
        driver.find_element_by_id("searchBtn").click()

        # Expected: 1 record back
        self.assertTrue(len(driver.find_elements_by_xpath("//td[3]/a")) == 1)


        # Expected Correct Full Name
        firstName = driver.find_element_by_xpath("//td[3]/a").text
        lastName = driver.find_element_by_xpath("//td[4]/a").text
        job_title = driver.find_element_by_xpath("//td[5]").text
        employment_status = driver.find_element_by_xpath("//td[6]").text


        message = "Expected the table to contain first name '{0}' but instead the value was '{1}'"
        self.assertEqual(expected_first_name, firstName, message.format(expected_first_name, firstName))
        self.assertEqual(expected_last_name, lastName)
        self.assertEqual(expected_job_title, job_title)
        self.assertEqual(expected_employment_status, employment_status)

        # logout
        # driver.find_element_by_id('welcome').click()
        # self.wait.until(expected_conditions.visibility_of_element_located((By.LINK_TEXT, 'Logout'))).click()
        logout(driver)

        # login
        login(driver, username)

        # check welcome message
        self.assertEqual('Welcome ' + expected_first_name, get_welcome_message(driver))

        # logout
        # driver.find_element_by_id('welcome').click()
        # self.wait.until(expected_conditions.visibility_of_element_located((By.LINK_TEXT, 'Logout'))).click()
        logout(driver)


if __name__ == '__main__':
    unittest.main()
