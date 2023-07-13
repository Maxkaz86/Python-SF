import pytest
from selenium import webdriver
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

class HomePage:
    def __init__(self, driver):
        self.driver = driver
        self.market_banner_locator = (By.XPATH, "//div[@class='btn btnOrange btnFlat js-popup-close']")
        self.destination_locator = (By.NAME, 'destination')
        self.button_click_locator = (By.ID, 'startSearch')

    def search_of_destination(self, destination_text):
        # self.driver.implicitly_wait(5)
        market_banner = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(self.market_banner_locator))
        market_banner.click()
        destination = self.driver.find_element(self.destination_locator)
        destination.clear()
        destination.send_keys(destination_text)
        time.sleep(3)
        button_click = self.driver.find_element(self.button_click_locator)
        button_click.click()

@pytest.fixture(scope='session')
def selenium_driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.implicitly_wait(10)

    yield driver

    driver.quit()

def test_search_for_destination(selenium_driver):
    selenium_driver.get('https://travelata.ru/')
    home_page = HomePage(selenium_driver)
    home_page.search_of_destination('Самара')


