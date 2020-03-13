from selenium.webdriver.common.by import By
from web.pages.base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def go_to_catalouge(self):
        link = self.driver.find_element(*ProductPageLocators.ADD_TO_BASCKET)
        link.click()







