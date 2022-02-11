from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from traceback import print_stack
import logging
import utils.custom_logger as cl
import time
import os
import pytest
from selenium.webdriver.common.action_chains import ActionChains


class BasePage():

    log = cl.CustomLogger()

    def __init__(self, driver):
        self.driver = driver
        self.base_url = 'https://console.argyle.io'

    def go_to(self, url):
        self.driver.get(url)

    def go_to_test_url(self):
        self.driver.get(self.base_url)

    def get_element(self, locator):
        element = None
        try:
            element = self.driver.find_element(*locator)
            self.log.info(f"Element {locator[1]} found...")
        except:
            self.log.error(f"Element {locator[1]} not found...")
            raise
        return element

    def get_elements(self, locator):
        
        elements = self.driver.find_elements(*locator)
        if len(elements) > 0:
            self.log.info(f"Element {locator[1]} found...")
            return elements
        else:
            self.log.error(f"Element {locator[1]} not found...")
            return None
            

    def click_on(self, locator):
        try:
            element = self.get_element(locator)
            element.click()
            self.log.info("Clicked on : "+str(locator[1]))
        except:
            self.log.error("Could not click on element: "+str(locator[1]))
            print_stack()
            raise
    
    def send_keys(self, locator, text=""):
        try:
            element = self.get_element(locator)
            element.send_keys(text)
            self.log.info("Keys sended to: " +str(locator[1]))
        except:
            self.log.error("Could not send keys to element: "+str(locator[1]))
            print_stack()
            raise

    def select_element_by_text(self, locator, text=""):
        try:
            element = self.get_element(locator)
            select = Select(element)
            select.select_by_visible_text(text)
            self.log.info("Selected element from menu: "+str(locator[1]))
        except:
            self.log.error("Could not select element: "+str(locator[1]))
            print_stack()
            raise

    def is_element_present(self, locator):

        element = self.get_element(locator)
        if element:
            self.log.info(f"Element {locator[1]} is present...")
            return True
        else:
            self.log.error(f"Element {locator[1]} not present...")
            return False


    def wait_element(self, locator, timeout=20):
        element = None
        try:
            self.log.info("Waiting for :: " + str(timeout) + " :: seconds for element")
            element = WebDriverWait(self.driver,timeout).until(EC.presence_of_element_located(locator))
        except:
            self.log.error("Element not found: "+str(locator[1]))
            print_stack()
        return element

    def get_element_size(self, locator):
        self.log.info(f"Trying to get element {locator[1]} size...")
        el = self.get_element(locator)
        return el.size

    def get_element_attribute(self, locator, attribute):
        self.log.info(f"Trying to get element {locator[1]} attribute...")
        el = self.get_element(locator)
        return el.get_attribute(attribute)
    
    def get_element_text(self, locator):
        self.log.info(f"Trying to get element {locator[1]} text...")
        el = self.get_element(locator)
        return el.text

    def js_click(self, locator):
        self.log.info(f"Trying to click element {locator[1]} with js function...")
        el = self.get_element(locator)
        self.driver.execute_script("arguments[0].click();", el)
    
    def wait_element_to_have_text(self, locator):
        self.log.info(f"Waiting for element {locator[1]} text is not empty...")
        count = 0
        while self.get_element_text(locator) == '' and count < 10:
            time.sleep(0.5)
            count += 1

    def move_cursor_to_element(self, locator):
        self.log.info(f"Trying to move cursor to element {locator[1]}...")
        el = self.get_element(locator)
        hover = ActionChains(self.driver).move_to_element(el)
        hover.perform()