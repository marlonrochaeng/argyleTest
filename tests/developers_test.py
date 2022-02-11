import imp
from re import I
import pytest
from pages.home_page import HomePage
from pages.login_page import LoginPage
from pages.developers_page import DevelopersPage
import unittest


class TestSystemInfo(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def ClassSetup(self, BrowserSetUp):
        self.home_page = HomePage(self.driver)
        self.login_page = LoginPage(self.driver)
        self.dev_page = DevelopersPage(self.driver)

        self.login_page.go_to_test_url()
        
        yield

        self.driver.quit()

    def test_verify_system_info(self):
        self.login_page.do_login("alin+qa@argyle.com", "Password123!@#")

        self.home_page.go_to_system()

        assert self.dev_page.get_api_status == 'Operational'
        assert self.dev_page.get_api_uptime == '100.00% uptime over the past 90 days'

        assert self.dev_page.get_console_status == 'Operational'
        assert self.dev_page.get_console_uptime == '100.00% uptime over the past 90 days'

        assert self.dev_page.get_link_status == 'Operational'
        assert self.dev_page.get_link_uptime == '100.00% uptime over the past 90 days'
        