import time

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()


@pytest.fixture(scope='class', autouse=True)
def run_mark():
    # Переходим на страницу авторизации
    driver.get('http://petfriends.skillfactory.ru/login')
    # добавляем ожидание появления кнопки войти
    wait = WebDriverWait(driver, 10)
    wait.until(EC.visibility_of_element_located((By.XPATH, '//button[@type="submit"]')))
    # Вводим email
    driver.find_element(By.ID, 'email').send_keys('max@mail.ru')
    # Вводим пароль
    driver.find_element(By.ID, 'pass').send_keys('Maksim123')
    # Нажимаем на кнопку входа в аккаунт
    driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()

    yield

    driver.quit()


class TestLocators:

    def test_show_my_pets(self):
        # # Вводим email
        # driver.find_element(By.ID, 'email').send_keys('max@mail.ru')
        # # Вводим пароль
        # driver.find_element(By.ID, 'pass').send_keys('Maksim123')
        # # Нажимаем на кнопку входа в аккаунт
        # driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()
        # Проверяем, что мы оказались на главной странице пользователя
        assert driver.find_element(By.TAG_NAME, 'h1').text == "PetFriends"

    def test_my_pets(self):
        driver.find_element(By.CSS_SELECTOR, 'a[href="/my_pets"]').click()
        driver.implicitly_wait(10)
        cards = driver.find_elements(By.CSS_SELECTOR, 'tbody>tr')
        assert len(cards) == 8

    def test_images_numbers(self):
        driver.implicitly_wait(10)
        driver.find_element(By.CSS_SELECTOR, 'a[href="/my_pets"]').click()
        images = driver.find_elements(By.CSS_SELECTOR, 'img')
        count = 0
        for i in range(len(images)):
            if images[i].get_attribute('src') != '':
                count += 1
        assert count > 4

    def test_check_animal_data(self):
        driver.find_element(By.CSS_SELECTOR, 'a[href="/my_pets"]').click()
        driver.implicitly_wait(10)
        names = driver.find_elements(By.CSS_SELECTOR, 'div#all_my_pets > table > tbody > tr > td')
        for i in range(len(names)):
            parts = names[i].text.split(' ')
            assert len(parts[0]) > 0
            assert len(parts[1]) > 0
            assert len(parts[2]) > 0


