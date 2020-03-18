import time
from .pages.basket_page import BasketPage
from .pages.main_page import MainPage
from .pages.login_page import LoginPage
from .pages.base_page import BasePage
from .pages.locators import MainPageLocators
from .pages.locators import LoginPageLocators
from .pages.locators import BasketPageLocators


# def test_guest_cant_see_product_in_basket_opened_from_main_page(driver):
#     page = MainPage(driver, MainPageLocators.LINK)
#     page.open()
#     page.go_to_basket()

# def test_guest_cant_see_product_in_basket_opened_from_main_page(driver):
#     page = BasketPage(driver, BasketPageLocators.LINK)
#     page.open()
#     page.go_to_basket()
#     page.check_that_basket_is_empty()

# def test_guest_can_go_to_login_page(driver):
#     page = MainPage(driver, MainPageLocator.LINK)
#     page.open()
#     page.go_to_login_page()
#     login_page = LoginPage(driver, driver.current_url)
#     login_page.should_be_login_page()
#
# def test_guest_should_see_login_link(driver):
#     page = MainPage(driver, MainPageLocator.LINK)
#     page.open()
#     page.should_be_login_link()
#
# def test_guest_can_see_login(driver):
#     page = LoginPage(driver, LoginPageLocators.LINK)
#     page.open()
#     page.should_be_login_page()
#
# def test_guest_can_see_registration(driver):
#     page = LoginPage(driver, LoginPageLocators.LINK)
#     page.open()
#     page.should_be_register_form()
#
# def test_guest_current_url(driver):
#     page = LoginPage(driver, LoginPageLocators.LINK)
#     page.open()
#     page.should_be_login_url()
