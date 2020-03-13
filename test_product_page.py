import time

from .pages.product_page import ProductPage
from .pages.locators import ProductPageLocators


def test_guest_can_add_product_to_basket(driver):
    page = ProductPage(driver, ProductPageLocators.TEST_LINK)
    page.open()
    page.add_book_shellcoder()
    page.solve_quiz_and_get_code()
    page.should_be_name_of_book()
    page.should_be_same_amout_of_money()
    # time.sleep(20)
    page.go_to_bascket()



