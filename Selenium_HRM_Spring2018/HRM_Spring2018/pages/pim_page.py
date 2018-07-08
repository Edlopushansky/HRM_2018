from fixtures.params import DOMAIN
from pages.base_page import BasePage


class PIMPage(BasePage):

    def __init__(self, driver):
        super(PIMPage, self).__init__(driver)
        self.page_url = DOMAIN + '/symfony/web/index.php/pim/viewEmployeeList'

    def goto_reports(self):
        driver = self.driver
        driver.find_element_by_id("menu_pim_viewPimModule").click()
        driver.find_element_by_id("menu_core_viewDefinedPredefinedReports").click()
