from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os

class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.base_url = "https://www.demoblaze.com/index.html"

    def find_element(self, locator, time=10):
        return WebDriverWait(self.driver, time).until(EC.presence_of_element_located(locator))

    def find_elements(self, locator, time=10):
        return WebDriverWait(self.driver, time).until(EC.presence_of_all_elements_located(locator))

    def go_to_site(self):
        return self.driver.get(self.base_url)