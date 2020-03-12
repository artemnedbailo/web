from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert "login" in self.driver.current_url, "'login' not in current url"
        assert True

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_EMAIL), 'Login_mail link is not presented'
        assert self.is_element_present(*LoginPageLocators.REGISTRATION_PASSWORD), 'Login_password link is not presented'
        assert self.is_element_present(*LoginPageLocators.LOGIN_BUTTON), 'Login_button link is not presented'
        assert True

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTRATION_EMAIL), 'Login_mail link is not presented'
        assert self.is_element_present(*LoginPageLocators.REGISTRATION_PASSWORD), 'Login_password link is not presented'
        assert self.is_element_present(*LoginPageLocators.REGISTRATION_PASSWORD_REPEAT), 'Login_password_repeat link is not presented'
        assert self.is_element_present(*LoginPageLocators.REGISTRATION_BUTTON), 'Login_button link is not presented'
        assert True