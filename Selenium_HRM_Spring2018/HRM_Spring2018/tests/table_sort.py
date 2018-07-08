import random
import unittest

from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from fixtures.params import CHROME_EXECUTABLE_PATH, EXPLICIT_TIMEOUT
from steps.common import login, is_element_present


class TableSort(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(
            executable_path=CHROME_EXECUTABLE_PATH
        )
        self.wait = WebDriverWait(self.driver, EXPLICIT_TIMEOUT)

        self.driver.get("http://hrm.seleniumminutes.com/")

    def tearDown(self):
        self.driver.quit()

    def test_table_sort_by_name(self):
        driver = self.driver

        login(driver, password='Password')
        driver.find_element_by_id("menu_pim_viewPimModule").click()
        driver.find_element_by_xpath("//th[3]/a").click()

        self.wait.until(EC.presence_of_element_located((By.XPATH, "//th[3]/a[@class='ASC']")))

        previous_name = ''
        while True:
            all_name_elements = driver.find_elements_by_xpath("//td[3]/a")
            for name_element in all_name_elements:
                current_name = name_element.text

                self.assertGreaterEqual(current_name, previous_name)

                previous_name = current_name
            if not is_element_present(driver, By.CSS_SELECTOR, ".paging.top .desc"):
                break

            paging = driver.find_element_by_css_selector(".paging.top .desc").text
            paging_parts = paging.split(' of ')

            if paging_parts[-1] in paging_parts[0]:
                break

            driver.find_element_by_css_selector(".paging.top .next a").click()


if __name__ == '__main__':
    unittest.main()
