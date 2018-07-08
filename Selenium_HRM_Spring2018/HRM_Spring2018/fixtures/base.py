import unittest

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.wait import WebDriverWait

from fixtures.params import CHROME_EXECUTABLE_PATH, EXPLICIT_TIMEOUT, DOMAIN, BROWSER_TYPE, FIREFOX_EXECUTABLE_PATH
from pages.login_page import LoginPage
from steps.common import login


class BaseTestCase(unittest.TestCase):
    def get_browser(self):
        if BROWSER_TYPE.lower().find('chrome') >= 0:
            browser = webdriver.Chrome(executable_path=CHROME_EXECUTABLE_PATH)
        elif BROWSER_TYPE.lower().find('firefox') >= 0:
            browser = webdriver.Firefox(executable_path=FIREFOX_EXECUTABLE_PATH)
        else:
            raise Exception("I'm sorry '{0}' browser is not supported".format(BROWSER_TYPE))
        return browser

    def is_element_present(driver, by, locator):
        try:
            driver.find_element(by, locator)
            return True
        except NoSuchElementException:
            return False

    def setUp(self):
        self.driver = self.get_browser()
        self.wait = WebDriverWait(self.driver, EXPLICIT_TIMEOUT)

    def tearDown(self):
        self.driver.quit()



class AdminLoginTestCase(BaseTestCase):
    def setUp(self):
        super(AdminLoginTestCase, self).setUp()
        self.driver.get(DOMAIN)
        login(self.driver)

    def tearDown(self):
        super(AdminLoginTestCase, self).tearDown()



class POMAdminLoginTestCase(BaseTestCase):
    def setUp(self):
        super(POMAdminLoginTestCase, self).setUp()
        self.login = LoginPage(self.driver)
        self.login.goto_page()
        self.login.login()

    def tearDown(self):
        super(POMAdminLoginTestCase, self).tearDown()




if __name__ == '__main__':
    unittest.main()
