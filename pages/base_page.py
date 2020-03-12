from selenium.common.exceptions import NoSuchElementException
link = "http://selenium1py.pythonanywhere.com/"


class BasePage:
    def __init__(self, driver, link, timeout=10):
        self.driver = driver
        self.link = link

    def open(self):
        self.driver.get(self.link)

    def is_element_present(self, how, what):
        try:
            self.driver.find_element(how, what)
        except (NoSuchElementException):
            return False
        return True