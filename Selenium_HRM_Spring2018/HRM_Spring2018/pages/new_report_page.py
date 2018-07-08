from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support import expected_conditions as EC

from fixtures.params import DOMAIN
from pages.base_page import BasePage


class NewReportPage(BasePage):

    def __init__(self, driver):
        super(NewReportPage, self).__init__(driver)
        self.page_url = DOMAIN + '/symfony/web/index.php/core/definePredefinedReport'


    def set_name(self, report_name):
        self.wait.until(
            EC.presence_of_element_located((By.ID, "report_report_name"))).send_keys(report_name)

    def select_selection_criteria(self, param):
        driver = self.driver
        Select(driver.find_element_by_id("report_criteria_list")).select_by_visible_text(param)
        driver.find_element_by_id("btnAddConstraint").click()

    def select_display_field_groups(self, param):
        driver = self.driver
        Select(driver.find_element_by_id("report_display_groups")).select_by_visible_text(param)
        driver.find_element_by_id("btnAddDisplayGroup").click()

    def enable_display_fields(self):
        self.driver.find_element_by_id("display_group_1").click()

    def save(self):
        self.driver.find_element_by_id("btnSave").click()
