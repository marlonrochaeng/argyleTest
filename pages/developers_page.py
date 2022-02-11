from selenium.webdriver.common.by import By
from .base_page import BasePage


class DevelopersPage(BasePage):
    #locators
    _api_status = By.XPATH, '//*[@id="containerElement"]/div[2]/div[1]/div[2]/div[1]/div[1]/div[1]/div/div[2]'
    _api_uptime = By.XPATH, '//*[@id="containerElement"]/div[2]/div[1]/div[2]/div[1]/div[1]/div[2]'
    _console_status = By.XPATH, '//*[@id="containerElement"]/div[2]/div[1]/div[2]/div[2]/div[1]/div[1]/div/div[2]'
    _console_uptime = By.XPATH, '//*[@id="containerElement"]/div[2]/div[1]/div[2]/div[2]/div[1]/div[2]'
    _link_status = By.XPATH, '//*[@id="containerElement"]/div[2]/div[1]/div[2]/div[3]/div[1]/div[1]/div/div[2]'
    _link_uptime = By.XPATH, '//*[@id="containerElement"]/div[2]/div[1]/div[2]/div[3]/div[1]/div[2]'

    @property
    def get_api_status(self):
        self.wait_element_to_have_text(self._api_status)
        return self.get_element_text(self._api_status)
    
    @property
    def get_api_uptime(self):
        return self.get_element_text(self._api_uptime)

    @property
    def get_console_status(self):
        return self.get_element_text(self._console_status)
    
    @property
    def get_console_uptime(self):
        return self.get_element_text(self._console_uptime)

    @property
    def get_link_status(self):
        return self.get_element_text(self._link_status)
    
    @property
    def get_link_uptime(self):
        return self.get_element_text(self._link_uptime)
