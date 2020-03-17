from .base_page import BasePage
from .locators import BasketPageLocators
from .main_page import MainPage

class BasketPage(BasePage):

    def check_that_basket_is_empty(self):
        check_basket = self.driver.find_element(*BasketPageLocators.EMPTY_BASKET)
        assert check_basket.text == 'Ваша корзина пуста', "Should be same amount of money"






