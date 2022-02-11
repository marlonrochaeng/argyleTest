from selenium.webdriver.common.by import By
from .base_page import BasePage


class UsersPage(BasePage):
    #locators
    _users_line = By.XPATH, "//a[@data-hook='user-list-row-link']"

    def is_user_info_correct(self, name, type):
        self.wait_element_to_have_text(self._users_line)
        users = self.get_elements(self._users_line)

        for u in users:
            texts = u.text.split('\n')
            if name in texts and type in texts:
                return True
        return False
