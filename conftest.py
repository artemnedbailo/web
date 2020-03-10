import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def pytest_addoption(parser):
    parser.addoption('--browser_name', action='store', default=None,
                     help="Choose browser: chrome or firefox")
    parser.addoption('--language', action='store', default='language',
                     help='Choose language: en, ru, fr and etc')




@pytest.fixture(scope="function")
def driver(request):
    driver_name = request.config.getoption('browser_name')
    user_language = request.config.getoption('language')
    if driver_name == "chrome":
        options = Options()
        options.add_experimental_option('prefs', {'intl.accept_languages': 'language'})
        print("\nstart chrome browser for test..")
        driver = webdriver.Chrome(executable_path='C:/fl/firefox.chrome/chromedriver_80.exe', options=options)
    # elif browser_name == "firefox":
    #     print("\nstart firefox browser for test..")
    #     browser = webdriver.Firefox(options=options,)
    else:
        raise pytest.UsageError("--browser_name should be chrome or firefox")
    print("\nstart browser for test..")

    yield driver
    print("\nquit browser..")
    driver.quit()


