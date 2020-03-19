from .base_page import BasePage
from .locators import BasePageLocators
from .locators import ProductPageLocators
from .locators import LoginPageLocators
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoAlertPresentException
import math
import pytest

class ProductPage(BasePage):

    def add_book_shellcoder(self):
        link = self.driver.find_element(*ProductPageLocators.BUTTON_ADD_TO_BASKET)
        link.click()

    def insert_email(self):
        email = self.driver.find_element(*LoginPageLocators.REGISTRATION_EMAIL)
        email.send_keys('qwe@mail.com')

    def insert_password(self):
        email = self.driver.find_element(*LoginPageLocators.REGISTRATION_PASSWORD)
        email.send_keys('qweqweqwe')

    def insert_password_repeat(self):
        email = self.driver.find_element(*LoginPageLocators.REGISTRATION_PASSWORD_REPEAT)
        email.send_keys('qweqweqwe')

    def button_for_registratio(self):
        email = self.driver.find_element(*LoginPageLocators.REGISTRATION_BUTTON)
        email.click()

    def go_to_the_basket(self):
        button = self.driver.find_element(*BasePageLocators.BUTTON_GO_TO_BASKET)
        button.click()

    def should_be_same_name_of_book(self):
        """
        Check that book name from book and from message the same
        """
        book_name = self.driver.find_element(*ProductPageLocators.BOOK_NAME_BEFORE)
        book_name_after = self.driver.find_element(*ProductPageLocators.SUCCESS_MESSAGE_ABOUT_BOOK)
        assert book_name_after.text == book_name.text, "Name of book doesnt match with message"
        assert True

    def should_be_success_message(self):
        assert self.is_element_present(*ProductPageLocators.SUCCESS_MESSAGE_ABOUT_BOOK), \
            "Success message is presented"

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE_ABOUT_BOOK), \
            "Success message is presented, but should not be"

    def should_not_be_success_message_disappeared(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE_ABOUT_BOOK), \
            "Success message is presented, but should not be"

    def should_be_same_amout_of_money(self):
        money_on_book = self.driver.find_element(*ProductPageLocators.PRICE_OF_BOOK)
        money_on_basket = self.driver.find_element(*ProductPageLocators.SUM_OF_MONEY_IN_BASKET)
        assert money_on_book.text == money_on_basket.text, "Should be same amount of money"

    def should_click_to_login_link(self):
        button = self.driver.find_element(*BasePageLocators.LOGIN_LINK)
        button.click()



