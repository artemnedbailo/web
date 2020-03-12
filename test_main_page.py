from .pages.main_page import MainPage
from .pages.locators import MainPageLocator



def test_guest_can_go_to_login_page(driver):
    page = MainPage(driver, MainPageLocator.LINK)
    page.open()
    page.go_to_login_page()

def test_guest_should_see_login_link(driver):
    page = MainPage(driver, MainPageLocator.LINK)
    page.open()
    page.should_be_login_link()