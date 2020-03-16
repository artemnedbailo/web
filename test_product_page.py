import time
import pytest
from .pages.product_page import ProductPage
from .pages.locators import ProductPageLocators

# product_base_link = ProductPageLocators.TEST_LINK_WITHOUT_POPUP
# urls = [f"{product_base_link}/?promo=offer{num}" for num in range[10]]

# @pytest.mark.parametrize('link', ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0",
#                                   "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1",
#                                   "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2",
#                                   "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3",
#                                   "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4",
#                                   "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5",
#                                   "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6",
#                                   pytest.param("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7",
#                                     marks=pytest.mark.xfail),
#                                   "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8",
#                                   "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9"])
# @pytest.mark.xfail(reason='shit happens')
# def test_guest_cant_see_success_message_after_adding_product_to_basket(driver):
#     page = ProductPage(driver, ProductPageLocators.TEST_LINK_WITH_POPUP)
#     page.open()
#     page.add_book_shellcoder()
#     page.solve_quiz_and_get_code()
#     page.should_not_be_success_message()
#
# def test_guest_cant_see_success_message(driver):
#     page = ProductPage(driver, ProductPageLocators.TEST_LINK_WITH_POPUP)
#     page.open()
#     page.should_not_be_success_message()
#
# @pytest.mark.xfail(reason='shit happens')
# def test_message_disappeared_after_adding_product_to_basket(driver):
#     page = ProductPage(driver, ProductPageLocators.TEST_LINK_WITH_POPUP)
#     page.open()
#     page.add_book_shellcoder()
#     page.solve_quiz_and_get_code()
#     page.should_not_be_success_message_disappeared()

def test_guest_can_go_to_login_page_from_product_page(driver):
    page = ProductPage(driver, ProductPageLocators.TEST_LINK_NEW_FOR_CITY_AND_STARS)
    page.open()
    page.should_click_to_login_link()

# def test_guest_should_see_login_link_on_product_page(driver):
#     page = ProductPage(driver, ProductPageLocators.TEST_LINK_NEW_FOR_CITY_AND_STARS)
#     page.open()
#     page.should_be_login_link()


# def test_guest_can_add_product_to_basket(driver):
#     page = ProductPage(driver, ProductPageLocators.TEST_LINK_WITH_POPUP)
#     page.open()
#     page.add_book_shellcoder()
#     page.solve_quiz_and_get_code()
#     page.should_be_name_of_book()
#     page.should_be_same_amout_of_money()
#     # time.sleep(20)
#     page.go_to_bascket()
#
# def test_correct_message_must_be_displayed(driver):
#     page = ProductPage(driver, ProductPageLocators.TEST_LINK_WITH_POPUP)
#     page.open()
#     page.add_book_shellcoder()
#     page.solve_quiz_and_get_code()
#     page.should_not_be_success_message()
#
# def test_correct_message_must_be_not_displayed(driver):
#     page = ProductPage(driver, ProductPageLocators.TEST_LINK_WITH_POPUP)
#     page.open()
#     page.add_book_shellcoder()
#     page.solve_quiz_and_get_code()
#     page.should_be_success_message()


#
# def test_guest_can_add_product_to_basket(driver):
#     page = ProductPage(driver, ProductPageLocators.LINK)
#     page.open()
#     page.add_book_shellcoder()
#     page.solve_quiz_and_get_code()
#     page.should_be_name_of_book()
#     page.should_be_same_amout_of_money()
#     # time.sleep(20)
#     page.go_to_bascket()




