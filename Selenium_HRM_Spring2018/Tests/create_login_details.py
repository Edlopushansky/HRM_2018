import unittest
import random
from faker import Faker
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from common.common import login, get_welcome_message, logout


class CreateLogin(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome('/home/eduard/Selenium_HRM_Spring2018/chromedriver')
        self.driver.maximize_window()
        # url = 'http://hrm-online.portnov.com'
        url = 'http://hrm.seleniumminutes.com'
        self.driver.get(url)
        self.wait = WebDriverWait(self.driver, 25)

    def test_create_login(self):

        empId = random.randint(100000, 9999999)
        fake = Faker()
        first_name = fake.first_name()
        last_name = fake.last_name()

        driver = self.driver

        login(driver)

        welcome_text = get_welcome_message(driver)
        self.assertEqual('Welcome Admin', welcome_text)

        driver.find_element_by_id('menu_pim_viewPimModule').click()
        driver.find_element_by_id('btnAdd').click()

        driver.find_element_by_id('firstName').send_keys(first_name)
        driver.find_element_by_id('lastName').send_keys(last_name)
        driver.find_element_by_id('employeeId').clear()
        driver.find_element_by_id('employeeId').send_keys(empId)

        #click Create Login Details button
        driver.find_element_by_id('chkLogin').click()

        login_name = first_name[0]+ last_name[0] + str(empId)


        #wait untill login name field is visible
        self.wait.until(EC.visibility_of_element_located((By.ID, 'user_name'))).send_keys(login_name)
        driver.find_element_by_id('user_password').send_keys('password')
        driver.find_element_by_id('re_password').send_keys('password')
        driver.find_element_by_id('btnSave').click()

        #logging out
        logout(driver)

        #login in with new credentials
        login(driver, login_name)

        #assert new Username welcome message
        self.assertEqual('Welcome ' + first_name, get_welcome_message(driver))

    def tearDown(self):
        self.driver.quit()

