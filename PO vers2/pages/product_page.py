from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class ProductPage(BasePage):
    LOCATOR_PRODUCT_NAME = (By.CLASS_NAME, 'name')

    def get_product_name(self):
        return self.find_element(self.LOCATOR_PRODUCT_NAME).text
