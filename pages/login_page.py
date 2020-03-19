from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def driver_quit(self):
        quit = self.driver.quit()

#4.3.13    def register_new_user(self, email, password):

    def insert_email(self):
        email = self.driver.find_element(*LoginPageLocators.REGISTRATION_EMAIL)
        email.send_keys('qwe@mail.com')

    def insert_password(self):
        email = self.driver.find_element(*LoginPageLocators.REGISTRATION_PASSWORD)
        email.send_keys('qweqweqwe')

    def insert_password_repeat(self):
        email = self.driver.find_element(*LoginPageLocators.REGISTRATION_PASSWORD_REPEAT)
        email.send_keys('qweqweqwe')

    def button_for_registration(self):
        email = self.driver.find_element(*LoginPageLocators.REGISTRATION_BUTTON)
        email.click()

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