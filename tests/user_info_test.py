from re import I
import pytest
from pages.home_page import HomePage
from pages.login_page import LoginPage
from pages.users_page import UsersPage
import unittest


class TestUserInfo(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def ClassSetup(self, BrowserSetUp):
        self.home_page = HomePage(self.driver)
        self.login_page = LoginPage(self.driver)
        self.users_page = UsersPage(self.driver)

        self.login_page.go_to_test_url()
        
        yield

        self.driver.quit()

    def test_verify_user_info(self):
        self.login_page.do_login("alin+qa@argyle.com", "Password123!@#")

        self.home_page.go_to_users()

        assert self.users_page.is_user_info_correct('Bob Jones', 'Sample user')
