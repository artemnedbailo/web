from .pages.main_page import MainPage
from .pages.login_page import LoginPage
from .pages.locators import MainPageLocator
from .pages.locators import LoginPageLocators



def test_guest_can_go_to_login_page(driver):
    page = MainPage(driver, MainPageLocator.LINK)
    page.open()
    page.go_to_login_page()

def test_guest_should_see_login_link(driver):
    page = MainPage(driver, MainPageLocator.LINK)
    page.open()
    page.should_be_login_link()

def test_guest_can_see_login(driver):
    page = LoginPage(driver, LoginPageLocators.LINK)
    page.open()
    page.should_be_login_form()

def test_guest_can_see_registration(driver):
    page = LoginPage(driver, LoginPageLocators.LINK)
    page.open()
    page.should_be_register_form()
