from selenium.webdriver.support.wait import WebDriverWait

from fixtures.params import EXPLICIT_TIMEOUT


class BasePage(object):

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, EXPLICIT_TIMEOUT)
        self.page_url = None

    def goto_page(self):
        if self.page_url is None:
            raise Exception('The goto_page() function for this page can only be used if the optional parameter was provided to the __init__ function of this page object')
        self.driver.get(self.page_url)