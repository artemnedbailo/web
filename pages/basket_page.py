from .base_page import BasePage
from .locators import BasketPageLocators

class BasketPage(BasePage):

    def check_that_basket_is_empty(self):
        check_basket = self.driver.find_element(*BasketPageLocators.EMPTY_BASKET)
        print(check_basket.text)
        assert check_basket.text == 'Your basket is empty. Continue shopping', "Should be same amount of money"






