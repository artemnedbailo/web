from .pages.product_page import ProductPage



def test_guest_can_go_to_login_page(driver):
    page = MainPage(driver, MainPageLocator.LINK)
    page.open()
    page.go_to_login_page()
    login_page = LoginPage(driver, driver.current_url)
    login_page.should_be_login_page()