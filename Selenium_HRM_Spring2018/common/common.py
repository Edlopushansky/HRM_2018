
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


def login(driver, username='admin', password= 'password'):
    if driver.current_url.find('seleniumminutes') > 0 and username == 'admin':
        password = password.title()
    driver.find_element_by_id('txtUsername').send_keys(username)
    driver.find_element_by_id('txtPassword').send_keys(password)
    driver.find_element_by_id('btnLogin').click()


def get_welcome_message(driver):
    return WebDriverWait(driver, 2).until(
        EC.presence_of_element_located((By.ID,'welcome'))).text


def logout(driver):
    driver.find_element_by_id('welcome').click()
    WebDriverWait(driver, 2).until(EC.visibility_of_element_located((By.LINK_TEXT, 'Logout'))).click()
