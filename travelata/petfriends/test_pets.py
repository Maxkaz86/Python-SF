from selenium.webdriver.common.by import By

BASE_URL = 'https://petfriends.skillfactory.ru/'

def test_show_my_pets(selenium_driver):
    driver = selenium_driver

    driver.find_element(By.CSS_SELECTOR, 'a.nav-link[href="/my_pets"]').click()
    assert driver.current_url == BASE_URL + 'my_pets'

    pets_number = driver.find_element(By.XPATH, '//div[@class=".col-sm-4 left"]').text.split('\n')[1].split(': ')[1]
    pets_count = driver.find_elements(By.XPATH, '//table[@class="table table-hover"]/tbody/tr')
    assert int(pets_number) == len(pets_count)