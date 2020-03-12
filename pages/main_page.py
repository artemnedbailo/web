from .base_page import BasePage
from selenium.webdriver.common.by import By
from .locators import MainPageLocator

class MainPage(BasePage):
    def go_to_login_page(self):
        login_link = self.driver.find_element(*MainPageLocator.LOGIN_LINK)
        login_link.click()

    def should_be_login_link(self):
        assert self.is_element_present(*MainPageLocator.LOGIN_LINK), 'Login link is not presented'

