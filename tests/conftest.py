import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


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
        chrome_options = Options()
        chrome_options.add_argument("--headless")
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--disable-dev-shm-usage")
        chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
        chrome_options.add_experimental_option('useAutomationExtension', False)
        driver = webdriver.Chrome(chrome_options=chrome_options)

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
