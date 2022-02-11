import pytest
from pages.home_page import HomePage
from pages.login_page import LoginPage
from pages.components.emulator_component import EmulatorComponent
import unittest


class TestEmulator(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def ClassSetup(self, BrowserSetUp):
        self.home_page = HomePage(self.driver)
        self.login_page = LoginPage(self.driver)
        self.emulator_comp = EmulatorComponent(self.driver)
        
        yield

        self.driver.quit()

    def test_send_code(self):
        self.login_page.go_to_test_url()
        self.login_page.do_login("alin+qa@argyle.com", "Password123!@#")

        self.home_page.go_to_emulator()

        self.emulator_comp.search_employer('Uber')
        self.emulator_comp.connect_to_employer('test1@argyle.com', 'passgood')
        self.emulator_comp.send_code()

        assert self.emulator_comp.is_confirm_msg_displayed()
        assert self.emulator_comp.get_status_msg == 'Your account was linked successfully.'


        