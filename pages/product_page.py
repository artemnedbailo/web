from web.pages.base_page import BasePage
from .locators import ProductPageLocators
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoAlertPresentException
import math


class ProductPage(BasePage):
    def add_book_shellcoder(self):
        link = self.driver.find_element(*ProductPageLocators.BUTTON_ADD_TO_BASKET)
        link.click()

    def go_to_bascket(self):
        button = self.driver.find_element(*ProductPageLocators.BUTTON_GO_TO_BASKET)
        button.click()

    def should_be_name_of_book(self):
        bookName = self.driver.find_element(*ProductPageLocators.BOOK_NAME_BEFORE)
        print('hello---------', bookName.text)
        bookNameAfter = self.driver.find_element(*ProductPageLocators.SUCCESS_MESSAGE_ABOUT_BOOK)
        assert bookNameAfter.text == bookName.text, "Name of book doesnt match with message"
        assert True

    def should_be_same_amout_of_money(self):
        moneyOnBook = self.driver.find_element(*ProductPageLocators.PRICE_OF_BOOK)
        moneyOnBasket = self.driver.find_element(*ProductPageLocators.SUM_OF_MONEY_IN_BASKET)
        print('hello---------', moneyOnBook)
        print('hello---------', moneyOnBasket)
        assert moneyOnBook.text == moneyOnBasket.text, "Should be same amount of money"





