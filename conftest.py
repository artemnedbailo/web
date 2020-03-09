import pytest
from selenium import webdriver

@pytest.fixture(scope="function")
def driver():
    print("\nstart browser for test..")
    driver = webdriver.Chrome(executable_path='C:/1/drivers/chrome_79.exe')
    yield driver
    print("\nquit browser..")
    driver.quit()