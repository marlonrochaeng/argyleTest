from re import S, search
from selenium.webdriver.common.by import By
from ..base_page import BasePage
from selenium.webdriver.common.keys import Keys

class EmulatorComponent(BasePage):
    #locators
    _employer_search = By.XPATH, "//input[@data-hook='search-input']"
    _employer_email = By.XPATH, "//input[@placeholder='Email']"
    _employer_pass = By.XPATH, "//input[@placeholder='Password']"
    _connect_btn = By.XPATH, "//div[@data-hook='connect-button']"
    _code_input = By.XPATH, "//input[@data-hook='mfa-code-input']"
    _sms_code = By.XPATH, "//div[@data-hook='test-credentials-sms-code']"
    _confirm_msg = By.XPATH, "//div[text()='Completed']"
    _status_msg = By.XPATH, "//span[@data-hook='status-message']"

    def _employer_result(self, search):
        return By.XPATH, f"//div[(@data-hook='partner-item-name') and (text() ='{search}')]"

    def search_employer(self, search):
        self.send_keys(self._employer_search, search)
        self.click_on(self._employer_result(search))

    def connect_to_employer(self, emp_email, emp_password):
        self.send_keys(self._employer_email, emp_email)
        self.send_keys(self._employer_pass, emp_password)
        self.click_on(self._connect_btn)
    
    def get_code(self):
        code = self.get_element_text(self._sms_code).split(' ')[-1]
        code = ''.join([str(i) for i in code[5:]])
        return code

    def send_code(self):
        self.send_keys(self._code_input, self.get_code())
        self.click_on(self._connect_btn)

    def is_confirm_msg_displayed(self):
        return self.wait_element(self._confirm_msg)

    @property
    def get_status_msg(self):
        self.wait_element_to_have_text(self._status_msg)
        return self.get_element_text(self._status_msg)
