import random
import unittest

from selenium import webdriver


# class Calculator(unittest.TestCase):
#     def setUp(self):
#         self.driver = webdriver.Chrome(
#             executable_path='/Users/ellie/Selenium/HRM_Spring2018/browser_drivers/chromedriver'
#         )
#         self.driver.get('http://www.math.com/students/calculators/source/basic.htm')
#
#     def tearDown(self):
#         self.driver.quit()
from fixtures.base import BaseTestCase


class Calculator(BaseTestCase):
    def setUp(self):
        super(Calculator,self).setUp()
        self.driver.get('http://www.math.com/students/calculators/source/basic.htm')

    def enter_random_number(self):
        num = random.randint(0, 999)
        list_of_numbers = list(str(num))

        for number in list_of_numbers:
            self.driver.find_element_by_css_selector('input[value="  {0}  "]'.format(number)).click()
        return num   # still an int


    def enter_single_numbers(self):
        num = 0
        for digit in range(random.randint(1,3)):
            number = random.randint(0, 9)
            self.driver.find_element_by_css_selector('input[value="  {0}  "]'.format(number)).click()
            num = (num * 10) + number
        return num   # still an int

    def test_add_numbers(self):
        driver = self.driver

        # num1 = random.randint(0, 9)
        # num2 = random.randint(0, 9)
        operator = random.choice(['+',' -','x',' /'])

        # driver.find_element_by_css_selector('input[value="  {0}  "]'.format(num1)).click()
        # num1 = self.enter_random_number()    # num1
        # OR
        num1 = self.enter_single_numbers()
        driver.find_element_by_css_selector('input[value="  {0}  "]'.format(operator)).click()
        # driver.find_element_by_css_selector('input[value="  {0}  "]'.format(num2)).click()
        # num2 = self.enter_random_number()    # num2
        # OR
        num2 = self.enter_single_numbers()
        driver.find_element_by_name('DoIt').click()
        result = driver.find_element_by_name('Input').get_attribute('value')

        if operator == '+':
            expected_result = num1 + num2
        elif operator == ' -':
            expected_result = num1 - num2
        elif operator == 'x':
            expected_result = num1 * num2
        else:
            if num2 is 0:
                expected_result = 'Infinity'
            else:
                expected_result = num1 / float(num2)

        # # OR quick alternative
        #
        # if operator == ' /' and num2 is 0:
        #     expected_result = 'Infinity'
        # else:
        #     expected_result = eval("{0} {1} float({2})".format(num1, '/', num2))

        result = result if result is 'Infinity' else float(result)
        self.assertEqual(expected_result, result)


if __name__ == '__main__':
    unittest.main()
