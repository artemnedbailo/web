from selenium.webdriver.support.wait import WebDriverWait
from web.pages.base_page import BasePage
from selenium.webdriver.support import expected_conditions as EC
from .locators import ProductPageLocators
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoAlertPresentException
import math


class ProductPage(BasePage):
    def add_book_shellcoder(self):
        link = self.driver.find_element(*ProductPageLocators.ADD_TO_BASCKET)
        link.click()

    def solve_quiz_and_get_code(self):
        alert = self.driver.switch_to.alert
        x = alert.text.split(" ")[2]
        answer = str(math.log(abs((12 * math.sin(float(x))))))
        alert.send_keys(answer)
        alert.accept()
        try:
            alert = self.driver.switch_to.alert
            alert_text = alert.text
            print(f"Your code: {alert_text}")
            alert.accept()
        except NoAlertPresentException:
            print("No second alert presented")

    def wait_until_element_presnt(self):
        assert WebDriverWait(self.driver, 3).until(EC.alert_is_present())








