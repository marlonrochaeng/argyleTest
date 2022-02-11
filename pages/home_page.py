from selenium.webdriver.common.by import By
from .base_page import BasePage


class HomePage(BasePage):
    #locators
    _argile_link_btn = By.XPATH, "//div[contains(text(),'Argyle Link')]"
    _emulator_btn = By.XPATH, "//div[contains(text(),'Emulator')]"
    _welcome_msg = By.XPATH, "//div[@data-hook='get-started-header']"
    _company_name = By.XPATH, "//div[@data-hook='company-menu-name-wrapper']"
    _logout_btn = By.XPATH, "//div[@data-hook='console-log-out']"
    _users_btn = By.XPATH, "//a[@data-hook='users']"
    _developers_btn = By.XPATH, "//button[@data-hook='developers']"
    _system_status = By.XPATH, "//a[@data-hook='systemstatus']"
    
    def go_to_emulator(self):
        self.click_on(self._argile_link_btn)
        self.click_on(self._emulator_btn)

    @property
    def welcome_message(self):
        self.wait_element_to_have_text(self._welcome_msg)
        return self.get_element_text(self._welcome_msg)
    
    def is_logged(self):
        return self.is_element_present(self._welcome_msg)

    def do_logout(self):
        self.move_cursor_to_element(self._company_name)
        self.click_on(self._logout_btn)

    def go_to_users(self):
        self.click_on(self._users_btn)

    def go_to_system(self):
        self.click_on(self._developers_btn)
        self.click_on(self._system_status)
