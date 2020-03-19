from selenium.common.exceptions import NoSuchElementException, NoAlertPresentException, TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import math
from .locators import BasePageLocators


class BasePage:
    def __init__(self, driver, link, timeout=10):
        """
        Instance Variable
        """
        self.driver = driver
        self.link = link

    def go_to_basket(self):
        button = self.driver.find_element(*BasePageLocators.BUTTON_GO_TO_BASKET)
        button.click()

    def go_to_login_page(self):
        """
        Transition to login page. Now invalid link could be replaced by valid 'LOGIN_LINK'
        """
        link = self.driver.find_element(*BasePageLocators.LOGIN_LINK)
        link.click()

    def is_element_present(self, how, what):
        """
        Element should be presented.
        Example for (how, what):
        (By.XPATH, '//*[@id="messages"]/div[1]/div/strong')
        (*ProductPageLocators.SUCCESS_MESSAGE_ABOUT_BOOK)
        """
        try:
            self.driver.find_element(how, what)
        except NoSuchElementException:
            return False
        return True

    def is_disappeared(self, how, what, timeout=4):
        try:
            WebDriverWait(self.driver, timeout, 1, TimeoutException). \
                until_not(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return False
        return True

    def is_not_element_present(self, how, what, timeout=4):
        try:
            WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return True
        return False

    def open(self):
        self.driver.get(self.link)

    def should_be_authorized_user(self):
        assert self.is_element_present(*BasePageLocators.USER_ICON), "User icon is not presented," \
                                                                     " probably unauthorised user"

    def solve_quiz_and_get_code(self):
        alert = self.driver.switch_to.alert
        x = alert.text.split(" ")[2]
        answer = str(math.log(abs((12 * math.sin(float(x))))))
        alert.send_keys(answer)
        alert.accept()
        try:
            WebDriverWait(self.driver, 3).until(EC.alert_is_present())
            alert = self.driver.switch_to.alert
            alert_text = alert.text
            print(f"Your code: {alert_text}")
            alert.accept()
        except TimeoutException:
            print("No second alert presented")

    def should_be_login_link(self):
        """
        Checking that login button is presented
        """
        assert self.is_element_present(*BasePageLocators.LOGIN_LINK), "Login link is not presented"



