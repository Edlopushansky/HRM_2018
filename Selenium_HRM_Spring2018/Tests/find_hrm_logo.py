import unittest
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait


class Logo_test(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome('/home/eduard/Selenium_HRM_Spring2018/Tests/browsers/chromedriver')
        self.driver.maximize_window()
        url = 'http://hrm-online.portnov.com'
        # url = 'http://hrm.seleniumminutes.com'
        self.driver.get(url)
        self.driver.find_element_by_id('txtUsername').send_keys('admin')
        self.driver.find_element_by_id('txtPassword').send_keys('password')
        self.driver.find_element_by_id('btnLogin').click()
        self.wait = WebDriverWait(self.driver, 25)

    def tearDown(self):
        self.driver.quit()




    def test_logo_location(self):
        driver = self.driver
        logo = driver.find_element_by_xpath("//div[@id = 'branding']//img")
        logo_size = logo.size

        self.assertEqual(56,logo_size.get('height'))
        self.assertTrue(283,logo_size.get('width'))
        self.assertDictEqual(logo_size,{'width': 283,'height':56})

        window_size = self.driver.get_window_size()
        logo_location = logo.location

        top_right_logo_corner_x_location = logo_size.get('width') + logo_location.get('x')

        self.assertTrue(top_right_logo_corner_x_location < ( window_size.get('width'))/2)








