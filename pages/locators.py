from selenium.webdriver.common.by import By
import pytest


class BasePageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LINK_FOR_PRODUCT_PAGE = 'http://selenium1py.pythonanywhere.com/ru/catalogue/the-shellcoders-handbook_209/?promo=newYear'
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")
    BUTTON_GO_TO_BASKET = (By.CSS_SELECTOR, '#default > header > div.page_inner > div > div.basket-mini.pull-right.hidden-xs > span > a')

class BasketPageLocators:
    LINK_MAIN_PAGE = "http://selenium1py.pythonanywhere.com/"
    LINK_PRODUCT_PAGE = 'http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/'
    EMPTY_BASKET = (By.XPATH, '//*[@id="content_inner"]/p')

class MainPageLocators:
    LINK = "http://selenium1py.pythonanywhere.com/"
    LOGIN_LINK = (By.CSS_SELECTOR, '#login_link')

class LoginPageLocators:
    LINK = "http://selenium1py.pythonanywhere.com/ru/accounts/login/"
    LOGIN_EMAIL = (By.CSS_SELECTOR, '#id_login-username')
    LOGIN_PASSWORD = (By.CSS_SELECTOR, '#id_login-password')
    LOGIN_BUTTON = (By.CSS_SELECTOR, '#login_form > button')

    REGISTRATION_EMAIL = (By.CSS_SELECTOR, '#id_registration-email')
    REGISTRATION_PASSWORD = (By.CSS_SELECTOR, '#id_registration-password1')
    REGISTRATION_PASSWORD_REPEAT = (By.CSS_SELECTOR, '#id_registration-password2')
    REGISTRATION_BUTTON = (By.CSS_SELECTOR, '#register_form > button')

class ProductPageLocators:
    LINK_MAIN_PAGE = 'http://selenium1py.pythonanywhere.com/ru/'
    EMPTY_BASKET = (By.CSS_SELECTOR, '#content_inner > p')
    TEST_LINK_NEW_FOR_CITY_AND_STARS = 'http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/'
    TEST_LINK_WITHOUT_POPUP = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'
    TEST_LINK_WITH_POPUP = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0'
    LINK = 'http://selenium1py.pythonanywhere.com/ru/catalogue/the-shellcoders-handbook_209/?promo=newYear'
    BUTTON_ADD_TO_BASKET = (By.CSS_SELECTOR, '#add_to_basket_form > button')
    BUTTON_GO_TO_BASKET = (By.CSS_SELECTOR, '#default > header > div.page_inner > div > div.basket-mini.pull-right.hidden-xs > span > a')
    SUCCESS_MESSAGE_ABOUT_BOOK = (By.XPATH, '//*[@id="messages"]/div[1]/div/strong')
    BOOK_NAME_BEFORE = (By.CSS_SELECTOR, '#content_inner > article > div.row > div.col-sm-6.product_main > h1')
    PRICE_OF_BOOK = (By.CSS_SELECTOR, '#content_inner > article > div.row > div.col-sm-6.product_main > p.price_color')
    SUM_OF_MONEY_IN_BASKET = (By.CSS_SELECTOR, '#messages > div.alert.alert-safe.alert-noicon.alert-info.fade.in > div > p:nth-child(1) > strong')

    # "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1",
    # "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2",
    # "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3",
    # "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4",
    # "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5",
    # "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6",
    # pytest.param("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7",
    #              marks=pytest.mark.xfail),
    # "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8",
    # "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9"

