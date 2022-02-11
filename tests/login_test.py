import imp
import pytest
from pages.home_page import HomePage
from pages.login_page import LoginPage
import unittest


class TestLogin(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def ClassSetup(self, BrowserSetUp):
        self.home_page = HomePage(self.driver)
        self.login_page = LoginPage(self.driver)

        self.login_page.go_to_test_url()
        
        yield

        self.driver.quit()

    def test_valid_login(self):
        self.login_page.do_login("alin+qa@argyle.com", "Password123!@#")

        assert self.home_page.is_logged()
        assert self.home_page.welcome_message == 'Welcome to Argyle, test'

    def test_invalid_login(self):
        self.login_page.do_login("alin+adadwa@argyle.com", "abcassword123!@#")

        assert self.login_page.error_message == 'Incorrect email or password'

    def test_logout(self):
        self.login_page.do_login("alin+qa@argyle.com", "Password123!@#")
        self.home_page.do_logout()

        assert self.login_page.is_in_login_page()
        