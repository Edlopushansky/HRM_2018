from fixtures.params import DOMAIN, DEFAULT_PASSWORD
from pages.base_page import BasePage


class LoginPage(BasePage):

    def __init__(self, driver):
        LoginPage.__init__(driver)
        self.page_url = DOMAIN + '/symfony/web/index.php/auth/login'



    def login(self, username='admin', password=DEFAULT_PASSWORD):
        driver = self.driver

    # No longer necessary, because if the user changes the DOMAIN,
    # they will also update the DEFAULT_PASSWORD in the params.py file
        # if driver.current_url.find('seleniumminutes') >= 0 and username == 'admin':
        #     password = password.title()

        driver.find_element_by_id('txtUsername').send_keys(username)
        driver.find_element_by_id('txtPassword').send_keys(password)
        driver.find_element_by_id('btnLogin').click()

    def get_warning_message(self):
        return self.driver.find_element_by_id('spanMessage').text