from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from fixtures.params import DOMAIN
from pages.base_page import BasePage


class ReportRunPage(BasePage):

    def __init__(self, driver, reportId=None):
        super(ReportRunPage, self).__init__(driver)
        self.page_url = None if not reportId else DOMAIN + '/symfony/web/index.php/core/displayPredefinedReport?reportId={0}'.format(reportId)

    def get_report_header(self):
        return self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '.head h1'))).text