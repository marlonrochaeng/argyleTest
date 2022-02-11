import pytest
from selenium import webdriver
from pages.login_page import LoginPage


driver = None
@pytest.fixture(scope='function')
def BrowserSetUp(request, browser):
    print("Running browser setUp")
    global driver
    if browser == 'firefox':
        print("Tests will be executed on Firefox")
        driver = webdriver.Firefox()

    elif browser =='chrome':
        print("Tests will be executed on Chrome")
        driver = webdriver.Chrome("config/chromedriver")

    elif browser == 'safari':
        driver = webdriver.Safari()

    driver.maximize_window()
    driver.implicitly_wait(20)

    if request.cls:
        request.cls.driver = driver

    yield driver

def pytest_addoption(parser):
    parser.addoption("--browser")

@pytest.fixture(scope='session')
def browser(request):
    return request.config.getoption("--browser")
