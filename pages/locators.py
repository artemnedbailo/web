from selenium.webdriver.common.by import By


class MainPageLocator:
    LINK = "http://selenium1py.pythonanywhere.com/"
    LOGIN_LINK = (By.CSS_SELECTOR, '#login_link')
