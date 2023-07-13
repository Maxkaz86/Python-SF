from selenium import webdriver
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()

driver.get('https://travelata.ru/')

market_banner_locator = (By.XPATH, "//div[@class='btn btnOrange btnFlat js-popup-close']")
market_banner = WebDriverWait(driver, 10).until(EC.presence_of_element_located(market_banner_locator))
market_banner.click()

destination_locator = (By.NAME, 'destination')
destination = WebDriverWait(driver, 10).until(EC.presence_of_element_located(destination_locator))
destination.clear()
destination.send_keys('Самара')

button_click_locator = (By.ID, 'startSearch')
button_click = WebDriverWait(driver, 10).until(EC.presence_of_element_located(button_click_locator))
button_click.click()

time.sleep(3)

driver.quit()