import random
import unittest

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from fixtures.base import POMAdminLoginTestCase
from pages.reports_page import locators as RL
from pages.login_page import LoginPage
from pages.new_report_page import NewReportPage
from pages.pim_page import PIMPage
from pages.report_run_page import ReportRunPage
from pages.reports_page import ReportsPage
from steps.common import is_element_present


class ReportTestCase(POMAdminLoginTestCase):

    def setUp(self):
        super(ReportTestCase, self).setUp()

        # self.login_page = LoginPage(self.driver)    # is part of super().setUp()
        self.pim = PIMPage(self.driver)
        self.reports = ReportsPage(self.driver)
        self.new_report = NewReportPage(self.driver)
        self.report_run = ReportRunPage(self.driver)

    def tearDown(self):
        if self.report_name:
            self.pim.goto_reports()
            self.reports.search(self.report_name)
            self.reports.delete_report(self.report_name)

        super(ReportTestCase, self).tearDown()

    def test_create_report(self):
        report_name = 'EY Report #' + str(random.randint(1, 100))

        # self.login_page.login()    # is part of super().setUp()
        self.pim.goto_reports()
        self.reports.add()
        self.new_report.set_name(report_name)
        self.new_report.select_selection_criteria("Job Title")
        self.new_report.select_display_field_groups("Personal")
        self.new_report.enable_display_fields()
        self.new_report.save()
        self.report_name = report_name

        # just an example of using a locator inside a page object module
        print RL["search_button"][0], RL["search_button"][1]
        button_label = self.driver.find_element(RL["search_button"][0], RL["search_button"][1]).get_attribute('value')
        self.assertEqual('Search', button_label)
        #################

        self.reports.search(report_name)

        self.assertTrue(is_element_present(self.driver, By.XPATH, "//td[text()='{0}']".format(report_name)))

        self.reports.run(report_name)
        report_header = self.report_run.get_report_header()

        self.assertEqual('Report Name : {0}'.format(report_name), report_header)



if __name__ == '__main__':
    unittest.main()
