from .base_page import BasePage
from .login_page import LoginPage
from .locators import MainPageLocator
from selenium.webdriver.common.by import By

class MainPage(BasePage):
    def go_to_login_page(self):
        link = self.driver.find_element(*MainPageLocator.LOGIN_LINK)
        link.click()
        return LoginPage(driver=self.driver, link=self.driver.current_url)

    def should_be_login_link(self):
        assert self.is_element_present(*MainPageLocator.LOGIN_LINK), 'Login link is not presented'

