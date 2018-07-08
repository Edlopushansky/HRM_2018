from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from fixtures.params import DOMAIN
from pages.base_page import BasePage

locators = {
    "add_button": (By.ID, "btnAdd"),
    "search_textfield": (By.ID, "search_search"),
    "search_button": (By.CLASS_NAME, "searchBtn"),
    "delete_button": (By.ID, "btnDelete"),
    "dialog_delete_button": (By.ID, "dialogDeleteBtn")
}


class ReportsPage(BasePage):

    def __init__(self, driver):
        super(ReportsPage, self).__init__(driver)
        self.page_url = DOMAIN + '/symfony/web/index.php/core/viewDefinedPredefinedReports/reportGroup/3/reportType/PIM_DEFINED'

    def add(self):
        self.driver.find_element_by_id(locators["add_button"][1]).click()

    def search(self, report_name):
        driver = self.driver
        driver.find_element_by_id(locators["search_textfield"][1]).send_keys(report_name)
        driver.find_element_by_class_name(locators["search_button"][1]).click()

    def run(self, report_name):
        self.driver.find_element_by_xpath("//td[text()='{0}']/../td[3]/a".format(report_name)).click()

    def delete_report(self, report_name):
        driver = self.driver

        self.wait.until(EC.presence_of_element_located((By.XPATH, "//td[text()='{0}']/..//input".format(report_name)))).click()
        driver.find_element_by_id(locators["delete_button"][1]).click()

        self.wait.until(EC.visibility_of_element_located((By.ID, locators["dialog_delete_button"][1]))).click()
