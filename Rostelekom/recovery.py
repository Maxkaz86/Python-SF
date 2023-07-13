import pytest
import time
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from data import numb, numbN, KirE, ML

driver = webdriver.Chrome()
action = ActionChains(driver)

@pytest.fixture(autouse=True)
def testing():
    pytest.driver = webdriver.Chrome(r'C:\Chrome\chromedriver.exe')
    pytest.driver.get('https://b2c.passport.rt.ru/auth/realms/b2c/protocol/openid-connect/auth?client_id=account_b2c&redirect_uri=https://b2c.passport.rt.ru/account_b2c/login&response_type=code&scope=openid&state=4f836607-d705-4428-898c-dd0d3a4d4fa2&theme&auth_type')

    yield

    pytest.driver.quit()


def double_click(name):
    pass


def test_log_Right():
    driver.implicitly_wait(10)
    WebDriverWait(pytest.driver, 10).until(EC.visibility_of_element_located((By.TAG_NAME, 'h1')))
    assert pytest.driver.find_element(By.TAG_NAME, 'h1').text == "Авторизация"

    print(' . ')


    time.sleep(2)

    pytest.driver.find_element(By.CSS_SELECTOR, "a#forgot_password").click()

    time.sleep(2)
    print('           ТЕСТИРОВАНИЕ СЦЕНАРИЯ ВОССТАНОВЛЕНИЯ ПАРОЛЯ')

    vos_r = pytest.driver.find_elements(By.CSS_SELECTOR, 'section#page-right')
    for i in range(len(vos_r)):
        parts_vs = vos_r[i].text.split(", ")
        print('Поле "Восстановление пароля" содержит: ', parts_vs)

    print('    Сценарий ввода номера телефона на вкладке "Телефон" ')

    nameV = pytest.driver.find_element(By.CSS_SELECTOR, 'input#username')
    time.sleep(2)
    nameV.send_keys(Keys.CONTROL + "A")
    nameV.send_keys(Keys.BACKSPACE)
    nameV.send_keys(numbN)
    nameV.send_keys(Keys.TAB)
    errnV = pytest.driver.find_elements(By.CSS_SELECTOR, 'section#page-right > div > div > div > form > div > div > span')
    for i in range(len(errnV)):
        parts_errnV = errnV[i].text.split(", ")
        print('текст ошибки при вводе номера телефона без одной цифры : ', parts_errnV)

    nameV = pytest.driver.find_element(By.CSS_SELECTOR, 'input#username')
    time.sleep(2)
    nameV.send_keys(Keys.CONTROL + "A")
    nameV.send_keys(Keys.BACKSPACE)
    nameV.send_keys(numb)
    nameV.send_keys(Keys.TAB)
    errnV = pytest.driver.find_elements(By.CSS_SELECTOR, 'section#page-right > div > div > div > form > div > div > span')
    for i in range(len(errnV)):
        parts_errnV = errnV[i].text.split(", ")
        print('текст ошибки при вводе ликвидного номера телефона : ', parts_errnV)

    print('    Сценарий ввода электронного адреса на вкладке "Почта" ')

    pytest.driver.find_element(By.CSS_SELECTOR, 'div#t-btn-tab-mail').click()
    EmV = pytest.driver.find_element(By.CSS_SELECTOR, 'input#username')
    time.sleep(2)
    EmV.send_keys(Keys.CONTROL + "A")
    EmV.send_keys(Keys.BACKSPACE)
    EmV.send_keys(KirE)
    EmV.send_keys(Keys.TAB)
    erreV = pytest.driver.find_elements(By.CSS_SELECTOR,'section#page-right > div > div > div > form > div > div > span')
    for i in range(len(erreV)):
        parts_erreV = erreV[i].text.split(", ")
        print('текст ошибки при вводе невалидного эл.адреса : ', parts_erreV)

    EmV = pytest.driver.find_element(By.CSS_SELECTOR, 'input#username')
    time.sleep(2)
    EmV.send_keys(Keys.CONTROL + "A")
    EmV.send_keys(Keys.BACKSPACE)
    EmV.send_keys(ML)
    EmV.send_keys(Keys.TAB)
    erreV = pytest.driver.find_elements(By.CSS_SELECTOR,'section#page-right > div > div > div > form > div > div > span')
    for i in range(len(erreV)):
        parts_erreV = erreV[i].text.split(", ")
        print('текст ошибки при вводе верного эл.адреса : ', parts_erreV)