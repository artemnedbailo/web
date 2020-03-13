from selenium.webdriver.common.by import By
from web.pages.base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def add_book_shellcoder(self):
        link = self.driver.find_element(*ProductPageLocators.ADD_TO_BASCKET)
        link.click()







