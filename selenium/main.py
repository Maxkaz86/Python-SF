import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()


@pytest.fixture(scope='class', autouse=True)
def run_mark():
    # Переходим на страницу авторизации
    driver.get('http://petfriends.skillfactory.ru/login')
    # Вводим email
    driver.find_element(By.ID, 'email').send_keys('max@mail.ru')
    # Вводим пароль
    driver.find_element(By.ID, 'pass').send_keys('Maksim123')
    # Нажимаем на кнопку входа в аккаунт
    driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()
    driver.find_element(By.CSS_SELECTOR, 'a[href="/my_pets"]').click()

    yield

    driver.quit()


def check_animal_data():
    names = driver.find_elements(By.CSS_SELECTOR, 'div#all_my_pets > table > tbody > tr > td')
    # a = []
    # for i in range(len(names)):
    #     parts = names[i].text.split(' ')
    #     a.append(parts[0])
    return names

print(check_animal_data())
