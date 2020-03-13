from .pages.product_page import ProductPage



def test_guest_can_go_to_catalogue_shellcoder_page(driver):
    page = ProductPage(driver, ProductPage.LINK)
    page.open()
    page.add_book_shellcoder()
