from selenium.webdriver.common.by import By
from .base_page import BasePage


class LoginPage(BasePage):
    #locators
    _email_field = By.ID, "sign-in-email-input"
    _pass_field = By.ID, "sign-in-password-input"
    _sign_in_btn = By.XPATH, "//div[contains(text(),'Sign in')]"
    _incorrect_info_msg = By.ID, "sign-in-password-input-helper"

    
    def do_login(self, email, password):
        self.send_keys(self._email_field, email)
        self.send_keys(self._pass_field, password)
        self.click_on(self._sign_in_btn)

    @property
    def error_message(self):
        self.wait_element_to_have_text(self._incorrect_info_msg)
        return self.get_element_text(self._incorrect_info_msg)

    def is_in_login_page(self):
        return self.is_element_present(self._email_field) and \
            self.is_element_present(self._pass_field)
