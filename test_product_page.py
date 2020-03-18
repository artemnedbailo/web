import time
import pytest
from .pages.base_page import BasePage
from web.pages.locators import BasePageLocators
from .pages.basket_page import BasketPage
from .pages.locators import BasketPageLocators
from .pages.product_page import ProductPage
from .pages.locators import ProductPageLocators

# urls = [f"{ProductPageLocators.TEST_LINK_WITHOUT_POPUP}?promo=offer{num}" for num in range(6,8)]
#
#
# @pytest.mark.parametrize('link', urls)
# def test_guest_can_add_product_to_basket(driver, link):
#     page = ProductPage(driver, link)
#     page.open()
#     page.add_book_shellcoder()
#     page.solve_quiz_and_get_code()
#     page.should_be_same_name_of_book()

def test_guest_cant_see_product_in_basket_opened_from_product_page(driver):
    page = BasketPage(driver, BasketPageLocators.LINK_PRODUCT_PAGE)
    page.open()
    page.go_to_basket()
    page.check_that_basket_is_empty()

def test_correct_message_must_be_displayed(driver):
    page = ProductPage(driver, ProductPageLocators.TEST_LINK_WITH_POPUP)
    page.open()
    page.add_book_shellcoder()
    page.solve_quiz_and_get_code()
    page.should_be_success_message()

@pytest.mark.xfail(reason='displayed as we wish')
def test_correct_message_must_be_not_displayed(driver):
    page = ProductPage(driver, ProductPageLocators.TEST_LINK_WITH_POPUP)
    page.open()
    page.add_book_shellcoder()
    page.solve_quiz_and_get_code()
    page.should_be_success_message()

def test_guest_can_go_to_login_page_from_product_page(driver):
    page = ProductPage(driver, ProductPageLocators.TEST_LINK_NEW_FOR_CITY_AND_STARS)
    page.open()
    page.should_click_to_login_link()

def test_guest_should_see_login_link_on_product_page(driver):
    page = ProductPage(driver, ProductPageLocators.TEST_LINK_NEW_FOR_CITY_AND_STARS)
    page.open()
    page.should_be_login_link()

def test_guest_can_add_product_to_basket(driver):
    page = ProductPage(driver, ProductPageLocators.TEST_LINK_WITH_POPUP)
    page.open()
    page.add_book_shellcoder()
    page.solve_quiz_and_get_code()
    page.should_be_name_of_book()
    page.should_be_same_amout_of_money()
    # time.sleep(20)
    page.go_to_basket()

@pytest.mark.xfail(reason='shit happens')
def test_guest_cant_see_success_message_after_adding_product_to_basket(driver):
    page = ProductPage(driver, ProductPageLocators.TEST_LINK_WITH_POPUP)
    page.open()
    page.add_book_shellcoder()
    page.solve_quiz_and_get_code()
    page.should_not_be_success_message()

def test_guest_cant_see_success_message(driver):
    page = ProductPage(driver, ProductPageLocators.TEST_LINK_WITH_POPUP)
    page.open()
    page.should_not_be_success_message()

def test_guest_can_add_product_to_basket(driver):
    page = ProductPage(driver, ProductPageLocators.LINK)
    page.open()
    page.add_book_shellcoder()
    page.solve_quiz_and_get_code()
    page.should_be_same_name_of_book()
    page.should_be_same_amout_of_money()
    # time.sleep(20)
    time.sleep(5)
    page.go_to_the_basket()
    time.sleep(5)

@pytest.mark.xfail(reason='shit happens')
def test_message_disappeared_after_adding_product_to_basket(driver):
    page = ProductPage(driver, ProductPageLocators.TEST_LINK_WITH_POPUP)
    page.open()
    page.add_book_shellcoder()
    page.solve_quiz_and_get_code()
    page.should_not_be_success_message_disappeared()




