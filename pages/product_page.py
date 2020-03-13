from web.pages.base_page import BasePage
from .locators import ProductPageLocators
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoAlertPresentException
import math


class ProductPage(BasePage):
    def add_book_shellcoder(self):
        link = self.driver.find_element(*ProductPageLocators.BUTTON_ADD_TO_BASCKET)
        link.click()

    def go_to_backet(self):
        button = self.driver.find_element(*ProductPageLocators.BUTTON_GO_TO_BASCKET)
        button.click()








