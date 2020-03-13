from .pages.product_page import ProductPage
from .pages.locators import ProductPageLocators


def test_guest_can_go_to_catalogue_shellcoder_page(driver):
    page = ProductPage(driver, ProductPageLocators.LINK)
    page.open()
    page.add_book_shellcoder()
    page.solve_quiz_and_get_code()


