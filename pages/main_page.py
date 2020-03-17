from .base_page import BasePage
from .login_page import LoginPage
from .basket_page import BasketPage
from .locators import MainPageLocators
from .locators import BasePageLocators
from selenium.webdriver.common.by import By

class MainPage(BasePage):
    # def __init__(self, *args, **kwargs):
    #     super(MainPage, self).__init__(*args, **kwargs)
    pass

    def open_basket_page(self):
        button_basket = self.driver.find_element(*BasePageLocators.BUTTON_GO_TO_BASKET)
        button_basket.click()

    # def go_to_login_page(self):
    #     link = self.driver.find_element(*MainPageLocator.LOGIN_LINK)
    #     link.click()
    #     # alert = self.driver.switch_to.alert  # обработка попап
    #     # alert.accept
    #     # return LoginPage(driver=self.driver, link=self.driver.current_url)  #
    #
    # def should_be_login_link(self):
    #     assert self.is_element_present(*MainPageLocator.LOGIN_LINK), 'Login link is not presented'

