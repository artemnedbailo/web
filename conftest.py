import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def pytest_addoption(parser):
    parser.addoption('--browser_name', action='store', default='chrome',
                     help="Choose browser: chrome or firefox")
    parser.addoption('--language', action='store', default='language',
                     help='Choose language: en, ru, fr and etc')

    parser.addoption("--headless", action="store", default="headless",
                     help="Is headless driver?")


@pytest.fixture(scope="function")
def driver(request):
    driver_name = request.config.getoption('browser_name')
    user_language = request.config.getoption('language')
    headless = request.config.getoption('--headless')

    if driver_name == "chrome":
        options = Options()
        # options.add_argument('headless')
        options.add_experimental_option('prefs', {'intl.accept_languages': 'language'})
        print("\nstart chrome browser for test..")
        # driver = webdriver.Chrome(executable_path='C:/fl/firefox.chrome/chromedriver_79.exe', options=options)
        driver = webdriver.Chrome(executable_path='C:/werq/brow/chromedriver.exe', options=options)
    # elif browser_name == "firefox":
    #     print("\nstart firefox browser for test..")
    #     browser = webdriver.Firefox(executable_path='', options=options)
    else:
        raise pytest.UsageError("--browser_name should be chrome or firefox")
    print("\nstart browser for test..")

    yield driver
    print("\nquit browser..")
    driver.quit()



