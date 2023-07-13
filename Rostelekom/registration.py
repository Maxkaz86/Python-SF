import pytest
import time
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from data import numb1, numb2,Pr20, PrNV, Pr21, PrL_V, Pr7, pr, PrK, nameJ, nameAL, nameAK, num1, nameAB, nameABK, num2, nameS, nameASK, nameAS, namePP, namePY, namePOP, nameB30, name30, name2t, nameZn, nameAr, nameC, nameSS, fam_V, numb3, num11, num12, num13, Lat11, KirE, SE, ArE, ChE, Ye, NE, T2T2, DlE505, ML


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

    pytest.driver.find_element(By.ID, "kc-register").click()

    time.sleep(2)
    print('ТЕСТИРОВАНИЕ СЦЕНАРИЯ РЕГИСТРАЦИИ')
    reg_r =  pytest.driver.find_elements(By.ID, 'page-right')
    for i in range(len(reg_r)):
        parts_rr = reg_r[i].text.split(", ")
        print('правая часть содержит: ', parts_rr)

    reg_l = pytest.driver.find_elements(By.ID, 'page-left')
    for i in range(len(reg_l)):
        parts_rl = reg_l[i].text.split(", ")
        print('левая часть содержит: ', parts_rl)

    time.sleep(2)

    print('                         Проверка строки для ввода имени на ограничения. Негативные тесты: ')

    name = pytest.driver.find_element(By.CSS_SELECTOR,'section#page-right > div > div > div > form > div > div > div > input')
    name.send_keys(nameJ)
    name.send_keys(Keys.TAB)
    err = pytest.driver.find_elements(By.CSS_SELECTOR, 'section#page-right > div > div > div > form > div > div > span')
    for i in range(len(err)):
        parts_err = err[i].text.split(", ")
        print('текст ошибки при вводе иероглифов: ', parts_err)

    name = pytest.driver.find_element(By.CSS_SELECTOR,'section#page-right > div > div > div > form > div > div > div > input')
    name.send_keys(Keys.CONTROL+"A")
    name.send_keys(Keys.BACKSPACE)
    name.send_keys(name2t)
    name.send_keys(Keys.TAB)
    err = pytest.driver.find_elements(By.CSS_SELECTOR, 'section#page-right > div > div > div > form > div > div > span')
    for i in range(len(err)):
        parts_err = err[i].text.split(", ")
        print('текст ошибки при вводе текста с двумя тире: ', parts_err)

    name = pytest.driver.find_element(By.CSS_SELECTOR, 'section#page-right > div > div > div > form > div > div > div > input')
    time.sleep(2)
    name.send_keys(Keys.CONTROL + "A")
    name.send_keys(Keys.BACKSPACE)
    name.send_keys(numb1)
    name.send_keys(Keys.TAB)
    err = pytest.driver.find_elements(By.CSS_SELECTOR, 'section#page-right > div > div > div > form > div > div > span')
    for i in range(len(err)):
        parts_err = err[i].text.split(", ")
        print('текст ошибки при вводе номера телефона: ', parts_err)

    name = pytest.driver.find_element(By.CSS_SELECTOR, 'section#page-right > div > div > div > form > div > div > div > input')
    time.sleep(2)
    name.send_keys(Keys.CONTROL + "A")
    name.send_keys(Keys.BACKSPACE)
    name.send_keys(nameAL)
    name.send_keys(Keys.TAB)
    err = pytest.driver.find_elements(By.CSS_SELECTOR, 'section#page-right > div > div > div > form > div > div > span')
    for i in range(len(err)):
        parts_err = err[i].text.split(", ")
        print('текст ошибки при вводе одной латинской буквы А: ', parts_err)

    name = pytest.driver.find_element(By.CSS_SELECTOR,'section#page-right > div > div > div > form > div > div > div > input')
    time.sleep(2)
    name.send_keys(Keys.CONTROL + "A")
    name.send_keys(Keys.BACKSPACE)
    name.send_keys(nameAK)
    name.send_keys(Keys.TAB)
    err = pytest.driver.find_elements(By.CSS_SELECTOR, 'section#page-right > div > div > div > form > div > div > span')
    for i in range(len(err)):
        parts_err = err[i].text.split(", ")
        print('текст ошибки при вводе одной буквы А кириллицей: ', parts_err)

    name = pytest.driver.find_element(By.CSS_SELECTOR,'section#page-right > div > div > div > form > div > div > div > input')
    time.sleep(2)
    name.send_keys(Keys.CONTROL + "A")
    name.send_keys(Keys.BACKSPACE)
    name.send_keys(num1)
    name.send_keys(Keys.TAB)
    err = pytest.driver.find_elements(By.CSS_SELECTOR, 'section#page-right > div > div > div > form > div > div > span')
    for i in range(len(err)):
        parts_err = err[i].text.split(", ")
        print('текст ошибки при вводе одной цифры: ', parts_err)

    name = pytest.driver.find_element(By.CSS_SELECTOR,'section#page-right > div > div > div > form > div > div > div > input')
    time.sleep(2)
    name.send_keys(Keys.CONTROL + "A")
    name.send_keys(Keys.BACKSPACE)
    name.send_keys(nameAB)
    name.send_keys(Keys.TAB)
    err = pytest.driver.find_elements(By.CSS_SELECTOR, 'section#page-right > div > div > div > form > div > div > span')
    for i in range(len(err)):
        parts_err = err[i].text.split(", ")
        print('текст ошибки при вводе АВ латинскими буквами: ', parts_err)

    name = pytest.driver.find_element(By.CSS_SELECTOR, 'section#page-right > div > div > div > form > div > div > div > input')
    time.sleep(2)
    name.send_keys(Keys.CONTROL + "A")
    name.send_keys(Keys.BACKSPACE)
    name.send_keys(nameS)
    name.send_keys(Keys.TAB)
    err = pytest.driver.find_elements(By.CSS_SELECTOR, 'section#page-right > div > div > div > form > div > div > span')
    for i in range(len(err)):
        parts_err = err[i].text.split(", ")
        print('текст ошибки при вводе кириллицей !А: ', parts_err)

    name = pytest.driver.find_element(By.CSS_SELECTOR,'section#page-right > div > div > div > form > div > div > div > input')
    time.sleep(2)
    name.send_keys(Keys.CONTROL + "A")
    name.send_keys(Keys.BACKSPACE)
    name.send_keys(nameAS)
    name.send_keys(Keys.TAB)
    err = pytest.driver.find_elements(By.CSS_SELECTOR, 'section#page-right > div > div > div > form > div > div > span')
    for i in range(len(err)):
        parts_err = err[i].text.split(", ")
        print('текст ошибки при вводе латиницей A-: ', parts_err)

    name = pytest.driver.find_element(By.CSS_SELECTOR,'section#page-right > div > div > div > form > div > div > div > input')
    time.sleep(2)
    name.send_keys(Keys.CONTROL + "A")
    name.send_keys(Keys.BACKSPACE)
    name.send_keys(namePP)
    name.send_keys(Keys.TAB)
    err = pytest.driver.find_elements(By.CSS_SELECTOR, 'section#page-right > div > div > div > form > div > div > span')
    if err in reg_r:
        for i in range(len(err)):
            parts_err = err[i].text.split(", ")
            print('текст ошибки при вводе двух пробелов: ', parts_err)
    else:
        print("!!!  При вводе двух пробелов в поле имени система не выдаёт ошибку")

    name = pytest.driver.find_element(By.CSS_SELECTOR,'section#page-right > div > div > div > form > div > div > div > input')
    time.sleep(2)
    name.send_keys(Keys.CONTROL + "A")
    name.send_keys(Keys.BACKSPACE)
    name.send_keys(namePY)
    name.send_keys(Keys.TAB)
    err = pytest.driver.find_elements(By.CSS_SELECTOR, 'section#page-right > div > div > div > form > div > div > span')
    if err in reg_r:
        for i in range(len(err)):
            parts_err = err[i].text.split(", ")
            print('текст ошибки если оставить поле пустым: ', parts_err)
    else:
        print("!!!  Если оставить поле пустым система не выдаёт ошибку")

    name = pytest.driver.find_element(By.CSS_SELECTOR,'section#page-right > div > div > div > form > div > div > div > input')
    time.sleep(2)
    name.send_keys(Keys.CONTROL + "A")
    name.send_keys(Keys.BACKSPACE)
    name.send_keys(nameB30)
    name.send_keys(Keys.TAB)
    err = pytest.driver.find_elements(By.CSS_SELECTOR, '#page-right > div > div > div > form > div.name-container > div.rt-input-container.rt-input-container--error > span')
    for i in range(len(err)):
        parts_err = err[i].text.split(", ")
        print('текст ошибки если ввести более 30 символов: ', parts_err)

    name = pytest.driver.find_element(By.CSS_SELECTOR, 'section#page-right > div > div > div > form > div > div > div > input')
    time.sleep(2)
    name.send_keys(Keys.CONTROL + "A")
    name.send_keys(Keys.BACKSPACE)
    name.send_keys(nameAr)
    name.send_keys(Keys.TAB)
    err = pytest.driver.find_elements(By.CSS_SELECTOR,'#page-right > div > div > div > form > div.name-container > div.rt-input-container.rt-input-container--error > span')
    for i in range(len(err)):
        parts_err = err[i].text.split(", ")
        print('текст ошибки если ввести имя арабскими символами: ', parts_err)

    name = pytest.driver.find_element(By.CSS_SELECTOR, 'section#page-right > div > div > div > form > div > div > div > input')
    time.sleep(2)
    name.send_keys(Keys.CONTROL + "A")
    name.send_keys(Keys.BACKSPACE)
    name.send_keys(nameC)
    name.send_keys(Keys.TAB)
    err = pytest.driver.find_elements(By.CSS_SELECTOR,'#page-right > div > div > div > form > div.name-container > div.rt-input-container.rt-input-container--error > span')
    for i in range(len(err)):
        parts_err = err[i].text.split(", ")
        print('текст ошибки если ввести имя китайскими символами: ', parts_err)

    name = pytest.driver.find_element(By.CSS_SELECTOR, 'section#page-right > div > div > div > form > div > div > div > input')
    time.sleep(2)
    name.send_keys(Keys.CONTROL + "A")
    name.send_keys(Keys.BACKSPACE)
    name.send_keys(nameZn)
    name.send_keys(Keys.TAB)
    err = pytest.driver.find_elements(By.CSS_SELECTOR, '#page-right > div > div > div > form > div.name-container > div.rt-input-container.rt-input-container--error > span')
    for i in range(len(err)):
        parts_err = err[i].text.split(", ")
        print('текст ошибки если ввести имя символами: ', parts_err)

    name = pytest.driver.find_element(By.CSS_SELECTOR, 'section#page-right > div > div > div > form > div > div > div > input')
    time.sleep(2)
    name.send_keys(Keys.CONTROL + "A")
    name.send_keys(Keys.BACKSPACE)
    name.send_keys(nameSS)
    name.send_keys(Keys.TAB)
    err = pytest.driver.find_elements(By.CSS_SELECTOR, '#page-right > div > div > div > form > div.name-container > div.rt-input-container.rt-input-container--error > span')
    for i in range(len(err)):
        parts_err = err[i].text.split(", ")
        print('текст ошибки если ввести имя спец.символами: ', parts_err)

    print('                           Проверка при вводе валидных значений в поле "Имя":')
    print(   'Произведены 4 теста: 1.две буквы кириллицей 2.буква А с тире кириллицей 3.текст из 30 символов 4. валидное значение с тире . Если какой-либо тест будет провален система выдаст ошибку ')

    name = pytest.driver.find_element(By.CSS_SELECTOR,'section#page-right > div > div > div > form > div > div > div > input')
    time.sleep(2)
    name.send_keys(Keys.CONTROL + "A")
    name.send_keys(Keys.BACKSPACE)
    name.send_keys(nameABK)
    name.send_keys(Keys.TAB)
    err = pytest.driver.find_elements(By.CSS_SELECTOR, 'section#page-right > div > div > div > form > div > div > span')
    for i in range(len(err)):
        parts_err = err[i].text.split(", ")
        print('тест.1.текст ошибки при вводе АВ кириллицей: ', parts_err)

    name = pytest.driver.find_element(By.CSS_SELECTOR,'section#page-right > div > div > div > form > div > div > div > input')
    time.sleep(2)
    name.send_keys(Keys.CONTROL + "A")
    name.send_keys(Keys.BACKSPACE)
    name.send_keys(nameASK)
    name.send_keys(Keys.TAB)
    err = pytest.driver.find_elements(By.CSS_SELECTOR, 'section#page-right > div > div > div > form > div > div > span')
    for i in range(len(err)):
        parts_err = err[i].text.split(", ")
        print('тест.2.текст ошибки при вводе А и тире кириллицей: ', parts_err)

    name = pytest.driver.find_element(By.CSS_SELECTOR, 'section#page-right > div > div > div > form > div > div > div > input')
    time.sleep(2)
    name.send_keys(Keys.CONTROL + "A")
    name.send_keys(Keys.BACKSPACE)
    name.send_keys(name30)
    name.send_keys(Keys.TAB)
    err = pytest.driver.find_elements(By.CSS_SELECTOR, 'section#page-right > div > div > div > form > div > div > span')
    for i in range(len(err)):
        parts_err = err[i].text.split(", ")
        print('тест.3.текст ошибки при вводе 30 символов: ', parts_err)

    name = pytest.driver.find_element(By.CSS_SELECTOR,'section#page-right > div > div > div > form > div > div > div > input')
    time.sleep(2)
    name.send_keys(Keys.CONTROL + "A")
    name.send_keys(Keys.BACKSPACE)
    name.send_keys(namePOP)
    name.send_keys(Keys.TAB)
    err = pytest.driver.find_elements(By.CSS_SELECTOR, 'section#page-right > div > div > div > form > div > div > span')
    for i in range(len(err)):
        parts_err = err[i].text.split(", ")
        print('тест.4.текст ошибки при вводе валидного значения с тире: ', parts_err)

    print('                         Проверка строки для ввода фамилии на ограничения. Негативные тесты: ')

    family = pytest.driver.find_element(By.CSS_SELECTOR,
                                        'section#page-right > div > div > div > form > div > div:nth-of-type(2) > div > input')
    time.sleep(2)
    family.send_keys(Keys.CONTROL + "A")
    family.send_keys(Keys.BACKSPACE)
    family.send_keys(nameJ)
    family.send_keys(Keys.TAB)
    err = pytest.driver.find_elements(By.CSS_SELECTOR, 'section#page-right > div > div > div > form > div > div > span')
    for i in range(len(err)):
        parts_err = err[i].text.split(", ")
        print('текст ошибки при вводе японских символов: ', parts_err)

    family = pytest.driver.find_element(By.CSS_SELECTOR,
                                        'section#page-right > div > div > div > form > div > div:nth-of-type(2) > div > input')
    time.sleep(2)
    family.send_keys(Keys.CONTROL + "A")
    family.send_keys(Keys.BACKSPACE)
    family.send_keys(numb1)
    family.send_keys(Keys.TAB)
    err = pytest.driver.find_elements(By.CSS_SELECTOR, 'section#page-right > div > div > div > form > div > div > span')
    for i in range(len(err)):
        parts_err = err[i].text.split(", ")
        print('текст ошибки при вводе номера телефона: ', parts_err)

    family = pytest.driver.find_element(By.CSS_SELECTOR,
                                        'section#page-right > div > div > div > form > div > div:nth-of-type(2) > div > input')
    time.sleep(2)
    family.send_keys(Keys.CONTROL + "A")
    family.send_keys(Keys.BACKSPACE)
    family.send_keys(nameAL)
    family.send_keys(Keys.TAB)
    err = pytest.driver.find_elements(By.CSS_SELECTOR, 'section#page-right > div > div > div > form > div > div > span')
    for i in range(len(err)):
        parts_err = err[i].text.split(", ")
        print('текст ошибки при вводе одной латинской буквы: ', parts_err)

    family = pytest.driver.find_element(By.CSS_SELECTOR,
                                        'section#page-right > div > div > div > form > div > div:nth-of-type(2) > div > input')
    time.sleep(2)
    family.send_keys(Keys.CONTROL + "A")
    family.send_keys(Keys.BACKSPACE)
    family.send_keys(nameAK)
    family.send_keys(Keys.TAB)
    err = pytest.driver.find_elements(By.CSS_SELECTOR, 'section#page-right > div > div > div > form > div > div > span')
    for i in range(len(err)):
        parts_err = err[i].text.split(", ")
        print('текст ошибки при вводе одной буквы кириллицей: ', parts_err)

    family = pytest.driver.find_element(By.CSS_SELECTOR,
                                        'section#page-right > div > div > div > form > div > div:nth-of-type(2) > div > input')
    time.sleep(2)
    family.send_keys(Keys.CONTROL + "A")
    family.send_keys(Keys.BACKSPACE)
    family.send_keys(num1)
    family.send_keys(Keys.TAB)
    err = pytest.driver.find_elements(By.CSS_SELECTOR, 'section#page-right > div > div > div > form > div > div > span')
    for i in range(len(err)):
        parts_err = err[i].text.split(", ")
        print('текст ошибки при вводе одной цифры: ', parts_err)

    family = pytest.driver.find_element(By.CSS_SELECTOR,
                                        'section#page-right > div > div > div > form > div > div:nth-of-type(2) > div > input')
    time.sleep(2)
    family.send_keys(Keys.CONTROL + "A")
    family.send_keys(Keys.BACKSPACE)
    family.send_keys(nameAB)
    family.send_keys(Keys.TAB)
    err = pytest.driver.find_elements(By.CSS_SELECTOR, 'section#page-right > div > div > div > form > div > div > span')
    for i in range(len(err)):
        parts_err = err[i].text.split(", ")
        print('текст ошибки при вводе двух латинских букв: ', parts_err)

    family = pytest.driver.find_element(By.CSS_SELECTOR,
                                        'section#page-right > div > div > div > form > div > div:nth-of-type(2) > div > input')
    time.sleep(2)
    family.send_keys(Keys.CONTROL + "A")
    family.send_keys(Keys.BACKSPACE)
    family.send_keys(num2)
    family.send_keys(Keys.TAB)
    err = pytest.driver.find_elements(By.CSS_SELECTOR, 'section#page-right > div > div > div > form > div > div > span')
    for i in range(len(err)):
        parts_err = err[i].text.split(", ")
        print('текст ошибки при вводе двух цифр: ', parts_err)

    family = pytest.driver.find_element(By.CSS_SELECTOR,
                                        'section#page-right > div > div > div > form > div > div:nth-of-type(2) > div > input')
    time.sleep(2)
    family.send_keys(Keys.CONTROL + "A")
    family.send_keys(Keys.BACKSPACE)
    family.send_keys(nameS)
    family.send_keys(Keys.TAB)
    err = pytest.driver.find_elements(By.CSS_SELECTOR, 'section#page-right > div > div > div > form > div > div > span')
    for i in range(len(err)):
        parts_err = err[i].text.split(", ")
        print('текст ошибки при вводе "!А" кириллицей: ', parts_err)

    family = pytest.driver.find_element(By.CSS_SELECTOR,
                                        'section#page-right > div > div > div > form > div > div:nth-of-type(2) > div > input')
    time.sleep(2)
    family.send_keys(Keys.CONTROL + "A")
    family.send_keys(Keys.BACKSPACE)
    family.send_keys(nameS)
    family.send_keys(Keys.TAB)
    err = pytest.driver.find_elements(By.CSS_SELECTOR, 'section#page-right > div > div > div > form > div > div > span')
    for i in range(len(err)):
        parts_err = err[i].text.split(", ")
        print('текст ошибки при вводе "!А" кириллицей: ', parts_err)

    family = pytest.driver.find_element(By.CSS_SELECTOR,
                                        'section#page-right > div > div > div > form > div > div:nth-of-type(2) > div > input')
    time.sleep(2)
    family.send_keys(Keys.CONTROL + "A")
    family.send_keys(Keys.BACKSPACE)
    family.send_keys(nameAS)
    family.send_keys(Keys.TAB)
    err = pytest.driver.find_elements(By.CSS_SELECTOR, 'section#page-right > div > div > div > form > div > div > span')
    for i in range(len(err)):
        parts_err = err[i].text.split(", ")
        print('текст ошибки при вводе "А-" латинскими: ', parts_err)

    family = pytest.driver.find_element(By.CSS_SELECTOR,
                                        'section#page-right > div > div > div > form > div > div:nth-of-type(2) > div > input')
    time.sleep(2)
    family.send_keys(Keys.CONTROL + "A")
    family.send_keys(Keys.BACKSPACE)
    family.send_keys(nameB30)
    family.send_keys(Keys.TAB)
    err = pytest.driver.find_elements(By.CSS_SELECTOR, 'section#page-right > div > div > div > form > div > div > span')
    for i in range(len(err)):
        parts_err = err[i].text.split(", ")
        print('текст ошибки при вводе более 30 символов кириллицей: ', parts_err)

    family = pytest.driver.find_element(By.CSS_SELECTOR,
                                        'section#page-right > div > div > div > form > div > div:nth-of-type(2) > div > input')
    time.sleep(2)
    family.send_keys(Keys.CONTROL + "A")
    family.send_keys(Keys.BACKSPACE)
    family.send_keys(name2t)
    family.send_keys(Keys.TAB)
    err = pytest.driver.find_elements(By.CSS_SELECTOR, 'section#page-right > div > div > div > form > div > div > span')
    for i in range(len(err)):
        parts_err = err[i].text.split(", ")
        print('текст ошибки при вводе валидного значения, но с 2 тире: ', parts_err)

    family = pytest.driver.find_element(By.CSS_SELECTOR,
                                        'section#page-right > div > div > div > form > div > div:nth-of-type(2) > div > input')
    time.sleep(2)
    family.send_keys(Keys.CONTROL + "A")
    family.send_keys(Keys.BACKSPACE)
    family.send_keys(nameAr)
    family.send_keys(Keys.TAB)
    err = pytest.driver.find_elements(By.CSS_SELECTOR, 'section#page-right > div > div > div > form > div > div > span')
    for i in range(len(err)):
        parts_err = err[i].text.split(", ")
        print('текст ошибки при вводе арабских символов: ', parts_err)

    family = pytest.driver.find_element(By.CSS_SELECTOR,
                                        'section#page-right > div > div > div > form > div > div:nth-of-type(2) > div > input')
    time.sleep(2)
    family.send_keys(Keys.CONTROL + "A")
    family.send_keys(Keys.BACKSPACE)
    family.send_keys(nameC)
    family.send_keys(Keys.TAB)
    err = pytest.driver.find_elements(By.CSS_SELECTOR, 'section#page-right > div > div > div > form > div > div > span')
    for i in range(len(err)):
        parts_err = err[i].text.split(", ")
        print('текст ошибки при вводе китайских символов: ', parts_err)

    family = pytest.driver.find_element(By.CSS_SELECTOR,
                                        'section#page-right > div > div > div > form > div > div:nth-of-type(2) > div > input')
    time.sleep(2)
    family.send_keys(Keys.CONTROL + "A")
    family.send_keys(Keys.BACKSPACE)
    family.send_keys(nameZn)
    family.send_keys(Keys.TAB)
    err = pytest.driver.find_elements(By.CSS_SELECTOR, 'section#page-right > div > div > div > form > div > div > span')
    for i in range(len(err)):
        parts_err = err[i].text.split(", ")
        print('текст ошибки при вводе символов: ', parts_err)

    family = pytest.driver.find_element(By.CSS_SELECTOR,
                                        'section#page-right > div > div > div > form > div > div:nth-of-type(2) > div > input')
    time.sleep(2)
    family.send_keys(Keys.CONTROL + "A")
    family.send_keys(Keys.BACKSPACE)
    family.send_keys(nameSS)
    family.send_keys(Keys.TAB)
    err = pytest.driver.find_elements(By.CSS_SELECTOR, 'section#page-right > div > div > div > form > div > div > span')
    for i in range(len(err)):
        parts_err = err[i].text.split(", ")
        print('текст ошибки при вводе спец.символов: ', parts_err)

    family = pytest.driver.find_element(By.CSS_SELECTOR, 'section#page-right > div > div > div > form > div > div:nth-of-type(2) > div > input')
    time.sleep(2)
    family.send_keys(Keys.CONTROL + "A")
    family.send_keys(Keys.BACKSPACE)
    family.send_keys(namePP)
    family.send_keys(Keys.TAB)
    err = pytest.driver.find_elements(By.CSS_SELECTOR, 'section#page-right > div > div > div > form > div > div > span')
    if err in reg_r:
        for i in range(len(err)):
            parts_err = err[i].text.split(", ")
            print('текст ошибки при вводе двух пробелов: ', parts_err)
    else:
        print("!!!  При вводе двух пробелов в поле имени система не выдаёт ошибку")

    family = pytest.driver.find_element(By.CSS_SELECTOR, 'section#page-right > div > div > div > form > div > div:nth-of-type(2) > div > input')
    time.sleep(2)
    family.send_keys(Keys.CONTROL + "A")
    family.send_keys(Keys.BACKSPACE)
    family.send_keys(namePY)
    family.send_keys(Keys.TAB)
    err = pytest.driver.find_elements(By.CSS_SELECTOR, 'section#page-right > div > div > div > form > div > div > span')
    if err in reg_r:
        for i in range(len(err)):
            parts_err = err[i].text.split(", ")
            print('текст ошибки если оставить поле пустым: ', parts_err)
    else:
        print("!!!  Если оставить поле пустым система не выдаёт ошибку")


    print('                           Проверка при вводе валидных значений в поле "Фамилия":')
    print(   'Произведены 4 теста: 1.две буквы кириллицей 2.буква А с тире кириллицей 3.текст из 30 символов 4. валидное значение с тире . Если какой-либо тест будет провален система выдаст ошибку ')

    family = pytest.driver.find_element(By.CSS_SELECTOR,
                                        'section#page-right > div > div > div > form > div > div:nth-of-type(2) > div > input')
    time.sleep(2)
    family.send_keys(Keys.CONTROL + "A")
    family.send_keys(Keys.BACKSPACE)
    family.send_keys(nameABK)
    family.send_keys(Keys.TAB)
    err = pytest.driver.find_elements(By.CSS_SELECTOR, 'section#page-right > div > div > div > form > div > div > span')
    for i in range(len(err)):
        parts_err = err[i].text.split(", ")
        print('тест.1.текст ошибки при вводе АВ кириллицей: ', parts_err)

    family = pytest.driver.find_element(By.CSS_SELECTOR,
                                        'section#page-right > div > div > div > form > div > div:nth-of-type(2) > div > input')
    time.sleep(2)
    family.send_keys(Keys.CONTROL + "A")
    family.send_keys(Keys.BACKSPACE)
    family.send_keys(nameASK)
    family.send_keys(Keys.TAB)
    err = pytest.driver.find_elements(By.CSS_SELECTOR, 'section#page-right > div > div > div > form > div > div > span')
    for i in range(len(err)):
        parts_err = err[i].text.split(", ")
        print('тест.2.текст ошибки при вводе А и тире кириллицей: ', parts_err)

    family = pytest.driver.find_element(By.CSS_SELECTOR,
                                        'section#page-right > div > div > div > form > div > div:nth-of-type(2) > div > input')
    time.sleep(2)
    family.send_keys(Keys.CONTROL + "A")
    family.send_keys(Keys.BACKSPACE)
    family.send_keys(name30)
    family.send_keys(Keys.TAB)
    err = pytest.driver.find_elements(By.CSS_SELECTOR, 'section#page-right > div > div > div > form > div > div > span')
    for i in range(len(err)):
        parts_err = err[i].text.split(", ")
        print('тест.3.текст ошибки при вводе 30 символов: ', parts_err)

    family = pytest.driver.find_element(By.CSS_SELECTOR,
                                        'section#page-right > div > div > div > form > div > div:nth-of-type(2) > div > input')
    time.sleep(2)
    family.send_keys(Keys.CONTROL + "A")
    family.send_keys(Keys.BACKSPACE)
    family.send_keys(fam_V)
    family.send_keys(Keys.TAB)
    err = pytest.driver.find_elements(By.CSS_SELECTOR, 'section#page-right > div > div > div > form > div > div > span')
    for i in range(len(err)):
        parts_err = err[i].text.split(", ")
        print('тест.4.текст ошибки при вводе валидного значения с тире: ', parts_err)

    print(                 'проверка выбора региона произведена вручную')

    time.sleep(10)
    print('              Проверка строки для ввода e-mail или мобильный телефон на ограничения. Негативные тесты: ')

    Mail = pytest.driver.find_element(By.ID, 'address')
    Mail.send_keys(num11)
    Mail.send_keys(Keys.TAB)
    errm = pytest.driver.find_elements(By.CSS_SELECTOR, 'section#page-right > div > div > div > form > div:nth-of-type(3) > div > span')
    for i in range(len(errm)):
        parts_errm = errm[i].text.split(", ")
        print('текст ошибки при вводе 11 цифр, не соответсвующих номеру телефона: ', parts_errm)

    Mail = pytest.driver.find_element(By.CSS_SELECTOR, 'input#address')
    time.sleep(1)
    Mail.send_keys(Keys.CONTROL + "A")
    Mail.send_keys(Keys.BACKSPACE)
    Mail.send_keys(num12)
    Mail.send_keys(Keys.TAB)
    errm = pytest.driver.find_elements(By.CSS_SELECTOR,'section#page-right > div > div > div > form > div:nth-of-type(3) > div > span')
    for i in range(len(errm)):
        parts_errm = errm[i].text.split(", ")
        print('текст ошибки при вводе 12 цифр, не соответсвующих номеру телефона: ', parts_errm)

    Mail = pytest.driver.find_element(By.CSS_SELECTOR, 'input#address')
    time.sleep(1)
    Mail.send_keys(Keys.CONTROL + "A")
    Mail.send_keys(Keys.BACKSPACE)
    Mail.send_keys(num13)
    Mail.send_keys(Keys.TAB)
    errm = pytest.driver.find_elements(By.CSS_SELECTOR,
                                       'section#page-right > div > div > div > form > div:nth-of-type(3) > div > span')
    for i in range(len(errm)):
        parts_errm = errm[i].text.split(", ")
        print('текст ошибки при вводе 13 цифр, не соответсвующих номеру телефона: ', parts_errm)

    Mail = pytest.driver.find_element(By.CSS_SELECTOR, 'input#address')
    time.sleep(1)
    Mail.send_keys(Keys.CONTROL + "A")
    Mail.send_keys(Keys.BACKSPACE)
    Mail.send_keys(Lat11)
    Mail.send_keys(Keys.TAB)
    errm = pytest.driver.find_elements(By.CSS_SELECTOR,
                                       'section#page-right > div > div > div > form > div:nth-of-type(3) > div > span')
    for i in range(len(errm)):
        parts_errm = errm[i].text.split(", ")
        print('текст ошибки при вводе 11 латинских букв ', parts_errm)

    Mail = pytest.driver.find_element(By.CSS_SELECTOR, 'input#address')
    time.sleep(1)
    Mail.send_keys(Keys.CONTROL + "A")
    Mail.send_keys(Keys.BACKSPACE)
    Mail.send_keys(KirE)
    Mail.send_keys(Keys.TAB)
    errm = pytest.driver.find_elements(By.CSS_SELECTOR,
                                       'section#page-right > div > div > div > form > div:nth-of-type(3) > div > span')
    for i in range(len(errm)):
        parts_errm = errm[i].text.split(", ")
        print('текст ошибки при вводе электронного адреса с буквами кириллицей', parts_errm)

    Mail = pytest.driver.find_element(By.CSS_SELECTOR, 'input#address')
    time.sleep(1)
    Mail.send_keys(Keys.CONTROL + "A")
    Mail.send_keys(Keys.BACKSPACE)
    Mail.send_keys(SE)
    Mail.send_keys(Keys.TAB)
    errm = pytest.driver.find_elements(By.CSS_SELECTOR,
                                       'section#page-right > div > div > div > form > div:nth-of-type(3) > div > span')
    for i in range(len(errm)):
        parts_errm = errm[i].text.split(", ")
        print('текст ошибки при вводе электронного адреса с символами и смайлами', parts_errm)

    Mail = pytest.driver.find_element(By.CSS_SELECTOR, 'input#address')
    time.sleep(1)
    Mail.send_keys(Keys.CONTROL + "A")
    Mail.send_keys(Keys.BACKSPACE)
    Mail.send_keys(ArE)
    Mail.send_keys(Keys.TAB)
    errm = pytest.driver.find_elements(By.CSS_SELECTOR,
                                       'section#page-right > div > div > div > form > div:nth-of-type(3) > div > span')
    for i in range(len(errm)):
        parts_errm = errm[i].text.split(", ")
        print('текст ошибки при вводе электронного адреса с арабскими символами', parts_errm)

    Mail = pytest.driver.find_element(By.CSS_SELECTOR, 'input#address')
    time.sleep(1)
    Mail.send_keys(Keys.CONTROL + "A")
    Mail.send_keys(Keys.BACKSPACE)
    Mail.send_keys(ChE)
    Mail.send_keys(Keys.TAB)
    errm = pytest.driver.find_elements(By.CSS_SELECTOR,
                                       'section#page-right > div > div > div > form > div:nth-of-type(3) > div > span')
    for i in range(len(errm)):
        parts_errm = errm[i].text.split(", ")
        print('текст ошибки при вводе электронного адреса с китайскими символами', parts_errm)

    Mail = pytest.driver.find_element(By.CSS_SELECTOR, 'input#address')
    time.sleep(1)
    Mail.send_keys(Keys.CONTROL + "A")
    Mail.send_keys(Keys.BACKSPACE)
    Mail.send_keys(Ye)
    Mail.send_keys(Keys.TAB)
    errm = pytest.driver.find_elements(By.CSS_SELECTOR,
                                       'section#page-right > div > div > div > form > div:nth-of-type(3) > div > span')
    for i in range(len(errm)):
        parts_errm = errm[i].text.split(", ")
        print('текст ошибки при вводе электронного адреса с японскими символами', parts_errm)

    Mail = pytest.driver.find_element(By.CSS_SELECTOR, 'input#address')
    time.sleep(1)
    Mail.send_keys(Keys.CONTROL + "A")
    Mail.send_keys(Keys.BACKSPACE)
    Mail.send_keys(NE)
    Mail.send_keys(Keys.TAB)
    errm = pytest.driver.find_elements(By.CSS_SELECTOR,
                                       'section#page-right > div > div > div > form > div:nth-of-type(3) > div > span')
    for i in range(len(errm)):
        parts_errm = errm[i].text.split(", ")
        print('текст ошибки при вводе электронного адреса прописанного буквами кириллицей', parts_errm)

    Mail = pytest.driver.find_element(By.CSS_SELECTOR, 'input#address')
    time.sleep(1)
    Mail.send_keys(Keys.CONTROL + "A")
    Mail.send_keys(Keys.BACKSPACE)
    Mail.send_keys(T2T2)
    Mail.send_keys(Keys.TAB)
    errm = pytest.driver.find_elements(By.CSS_SELECTOR,
                                       'section#page-right > div > div > div > form > div:nth-of-type(3) > div > span')
    for i in range(len(errm)):
        parts_errm = errm[i].text.split(", ")
        print('текст ошибки при вводе электронного адреса двумя точками и двумя тире', parts_errm)

    Mail = pytest.driver.find_element(By.CSS_SELECTOR, 'input#address')
    time.sleep(1)
    Mail.send_keys(Keys.CONTROL + "A")
    Mail.send_keys(Keys.BACKSPACE)
    Mail.send_keys(DlE505)
    Mail.send_keys(Keys.TAB)
    errm = pytest.driver.find_elements(By.CSS_SELECTOR,
                                       'section#page-right > div > div > div > form > div:nth-of-type(3) > div > span')
    if errm in reg_r:
        for i in range(len(errm)):
            parts_errm = errm[i].text.split(", ")
            print('текст ошибки при вводе очень длинного электронного адреса из 505 символов', parts_errm)
    else:
        print("!!!  ВВедено 505 символов, но система не выдаёт ошибку")


    print('                           Проверка при вводе валидных значений в поле "E-mail или номер телефона":')
    print(' Произведены 4 теста. 3 с разными форматами номера телефона и один с верным эл.адресом. Если какой-либо тест будет провален, система выдаст ошибку ')

    Mail = pytest.driver.find_element(By.CSS_SELECTOR, 'input#address')
    time.sleep(1)
    Mail.send_keys(Keys.CONTROL + "A")
    Mail.send_keys(Keys.BACKSPACE)
    Mail.send_keys(num1)
    Mail.send_keys(Keys.TAB)
    errm = pytest.driver.find_elements(By.CSS_SELECTOR,
                                       'section#page-right > div > div > div > form > div:nth-of-type(3) > div > span')
    for i in range(len(errm)):
        parts_errm = errm[i].text.split(", ")
        print('!!! не должно быть ошибки. введенный номер в формате 89xxxxxxxxx . система выдаёт ошибку:', parts_errm)

    Mail = pytest.driver.find_element(By.CSS_SELECTOR, 'input#address')
    time.sleep(1)
    Mail.send_keys(Keys.CONTROL + "A")
    Mail.send_keys(Keys.BACKSPACE)
    Mail.send_keys(numb2)
    Mail.send_keys(Keys.TAB)
    errm = pytest.driver.find_elements(By.CSS_SELECTOR,
                                       'section#page-right > div > div > div > form > div:nth-of-type(3) > div > span')
    for i in range(len(errm)):
        parts_errm = errm[i].text.split(", ")
        print('!!! не должно быть ошибки, номер указан верно, +79xxxxxxxxx, но система выдаёт ошибку:', parts_errm)

    Mail = pytest.driver.find_element(By.CSS_SELECTOR, 'input#address')
    time.sleep(1)
    Mail.send_keys(Keys.CONTROL + "A")
    Mail.send_keys(Keys.BACKSPACE)
    Mail.send_keys(numb3)
    Mail.send_keys(Keys.TAB)
    errm = pytest.driver.find_elements(By.CSS_SELECTOR,
                                       'section#page-right > div > div > div > form > div:nth-of-type(3) > div > span')
    for i in range(len(errm)):
        parts_errm = errm[i].text.split(", ")
        print('!!! не должно быть ошибки, номер указан верно, 9xxxxxxxxx, но система выдаёт ошибку:', parts_errm)

    Mail = pytest.driver.find_element(By.CSS_SELECTOR, 'input#address')
    time.sleep(1)
    Mail.send_keys(Keys.CONTROL + "A")
    Mail.send_keys(Keys.BACKSPACE)
    Mail.send_keys(ML)
    Mail.send_keys(Keys.TAB)
    errm = pytest.driver.find_elements(By.CSS_SELECTOR,
                                       'section#page-right > div > div > div > form > div:nth-of-type(3) > div > span')
    for i in range(len(errm)):
        parts_errm = errm[i].text.split(", ")
        print('!!! не должно быть ошибки, эл.адрес указан верно', parts_errm)

    print('              Проверка строки для ввода пароль на ограничения. Негативные тесты: ')

    Parol = pytest.driver.find_element(By.CSS_SELECTOR, 'input#password')
    time.sleep(1)
    Parol.send_keys(Keys.CONTROL + "A")
    Parol.send_keys(Keys.BACKSPACE)
    Parol.send_keys(nameAB)
    Parol.send_keys(Keys.TAB)
    errp = pytest.driver.find_elements(By.CSS_SELECTOR,
                                       'section#page-right > div > div > div > form > div:nth-of-type(4) > div > span')
    for i in range(len(errp)):
        partp_errp = errp[i].text.split(", ")
        print('текст ошибки при вводе двух латинских букв', partp_errp)

    Parol = pytest.driver.find_element(By.CSS_SELECTOR, 'input#password')
    time.sleep(1)
    Parol.send_keys(Keys.CONTROL + "A")
    Parol.send_keys(Keys.BACKSPACE)
    Parol.send_keys(nameABK)
    Parol.send_keys(Keys.TAB)
    errp = pytest.driver.find_elements(By.CSS_SELECTOR,
                                       'section#page-right > div > div > div > form > div:nth-of-type(4) > div > span')
    for i in range(len(errp)):
        partp_errp = errp[i].text.split(", ")
        print('текст ошибки при вводе двух букв кириллицей ', partp_errp)

    Parol = pytest.driver.find_element(By.CSS_SELECTOR, 'input#password')
    time.sleep(1)
    Parol.send_keys(Keys.CONTROL + "A")
    Parol.send_keys(Keys.BACKSPACE)
    Parol.send_keys(Pr7)
    Parol.send_keys(Keys.TAB)
    errp = pytest.driver.find_elements(By.CSS_SELECTOR,
                                       'section#page-right > div > div > div > form > div:nth-of-type(4) > div > span')
    for i in range(len(errp)):
        partp_errp = errp[i].text.split(", ")
        print('текст ошибки при вводе 7 латинских букв ', partp_errp)

    Parol = pytest.driver.find_element(By.CSS_SELECTOR, 'input#password')
    time.sleep(1)
    Parol.send_keys(Keys.CONTROL + "A")
    Parol.send_keys(Keys.BACKSPACE)
    Parol.send_keys(pr)
    Parol.send_keys(Keys.TAB)
    errp = pytest.driver.find_elements(By.CSS_SELECTOR,
                                       'section#page-right > div > div > div > form > div:nth-of-type(4) > div > span')
    for i in range(len(errp)):
        partp_errp = errp[i].text.split(", ")
        print('текст ошибки при вводе латинских букв без заглавной', partp_errp)

    Parol = pytest.driver.find_element(By.CSS_SELECTOR, 'input#password')
    time.sleep(1)
    Parol.send_keys(Keys.CONTROL + "A")
    Parol.send_keys(Keys.BACKSPACE)
    Parol.send_keys(PrK)
    Parol.send_keys(Keys.TAB)
    errp = pytest.driver.find_elements(By.CSS_SELECTOR,
                                       'section#page-right > div > div > div > form > div:nth-of-type(4) > div > span')
    for i in range(len(errp)):
        partp_errp = errp[i].text.split(", ")
        print('текст ошибки при вводе пароля с кириллицей: ', partp_errp)

    Parol = pytest.driver.find_element(By.CSS_SELECTOR, 'input#password')
    time.sleep(1)
    Parol.send_keys(Keys.CONTROL + "A")
    Parol.send_keys(Keys.BACKSPACE)
    Parol.send_keys(numb1)
    Parol.send_keys(Keys.TAB)
    errp = pytest.driver.find_elements(By.CSS_SELECTOR,
                                       'section#page-right > div > div > div > form > div:nth-of-type(4) > div > span')
    for i in range(len(errp)):
        partp_errp = errp[i].text.split(", ")
        print('текст ошибки при вводе номера телефона: ', partp_errp)

    Parol = pytest.driver.find_element(By.CSS_SELECTOR, 'input#password')
    time.sleep(1)
    Parol.send_keys(Keys.CONTROL + "A")
    Parol.send_keys(Keys.BACKSPACE)
    Parol.send_keys(nameC)
    Parol.send_keys(Keys.TAB)
    errp = pytest.driver.find_elements(By.CSS_SELECTOR,
                                       'section#page-right > div > div > div > form > div:nth-of-type(4) > div > span')
    for i in range(len(errp)):
        partp_errp = errp[i].text.split(", ")
        print('текст ошибки при вводе китайских символов: ', partp_errp)

    Parol = pytest.driver.find_element(By.CSS_SELECTOR, 'input#password')
    time.sleep(1)
    Parol.send_keys(Keys.CONTROL + "A")
    Parol.send_keys(Keys.BACKSPACE)
    Parol.send_keys(nameZn)
    Parol.send_keys(Keys.TAB)
    errp = pytest.driver.find_elements(By.CSS_SELECTOR,
                                       'section#page-right > div > div > div > form > div:nth-of-type(4) > div > span')
    for i in range(len(errp)):
        partp_errp = errp[i].text.split(", ")
        print('текст ошибки при вводе символов и смайлов: ', partp_errp)

    Parol = pytest.driver.find_element(By.CSS_SELECTOR, 'input#password')
    time.sleep(1)
    Parol.send_keys(Keys.CONTROL + "A")
    Parol.send_keys(Keys.BACKSPACE)
    Parol.send_keys(nameSS)
    Parol.send_keys(Keys.TAB)
    errp = pytest.driver.find_elements(By.CSS_SELECTOR,
                                       'section#page-right > div > div > div > form > div:nth-of-type(4) > div > span')
    for i in range(len(errp)):
        partp_errp = errp[i].text.split(", ")
        print('текст ошибки при вводе спец.символов: ', partp_errp)

    Parol = pytest.driver.find_element(By.CSS_SELECTOR, 'input#password')
    time.sleep(1)
    Parol.send_keys(Keys.CONTROL + "A")
    Parol.send_keys(Keys.BACKSPACE)
    Parol.send_keys(Pr21)
    Parol.send_keys(Keys.TAB)
    errp = pytest.driver.find_elements(By.CSS_SELECTOR,
                                       'section#page-right > div > div > div > form > div:nth-of-type(4) > div > span')
    for i in range(len(errp)):
        partp_errp = errp[i].text.split(", ")
        print('текст ошибки при вводе 21 латинских букв: ', partp_errp)

    print('                           Проверка при вводе валидных значений в поле "пароль":')
    print('Произведены 2 теста с валидными паролями. Если какой-либо тест будет провален, система выдаст ошибку ')

    Parol = pytest.driver.find_element(By.CSS_SELECTOR, 'input#password')
    time.sleep(1)
    Parol.send_keys(Keys.CONTROL + "A")
    Parol.send_keys(Keys.BACKSPACE)
    Parol.send_keys(Pr20)
    Parol.send_keys(Keys.TAB)
    errp = pytest.driver.find_elements(By.CSS_SELECTOR,
                                       'section#page-right > div > div > div > form > div:nth-of-type(4) > div > span')
    for i in range(len(errp)):
        partp_errp = errp[i].text.split(", ")
        print('!!!текст ошибки при вводе 20 латинских букв: ', partp_errp,
              ' не должно быть ошибки, т.к. по ТЗ условия соблюдены')

    Parol = pytest.driver.find_element(By.CSS_SELECTOR, 'input#password')
    time.sleep(1)
    Parol.send_keys(Keys.CONTROL + "A")
    Parol.send_keys(Keys.BACKSPACE)
    Parol.send_keys(PrL_V)
    Parol.send_keys(Keys.TAB)
    errp = pytest.driver.find_elements(By.CSS_SELECTOR,
                                       'section#page-right > div > div > div > form > div:nth-of-type(4) > div > span')
    for i in range(len(errp)):
        partp_errp = errp[i].text.split(", ")
        print('!!!текст ошибки при вводе валидного пароля с буквами и цифрами: ', partp_errp,
              ' не должно быть ошибки, т.к. по ТЗ условия соблюдены')

    print('                           Проверка строки для ввода "подтверждение пароля":')
    print("                     введено значение, отличающееся от того, что введенов поле'пароль' ")

    NParol = pytest.driver.find_element(By.CSS_SELECTOR, 'input#password-confirm')
    time.sleep(1)
    NParol.send_keys(Keys.CONTROL + "A")
    NParol.send_keys(Keys.BACKSPACE)
    NParol.send_keys(PrNV)
    but_reg = pytest.driver.find_element(By.CSS_SELECTOR, "section#page-right > div > div > div > form > button")
    but_reg.click()
    errnp = pytest.driver.find_elements(By.CSS_SELECTOR,
                                        'section#page-right > div > div > div > form > div:nth-of-type(4) > div:nth-of-type(2) > span')
    for i in range(len(errnp)):
        partp_errnp = errnp[i].text.split(", ")
        print('текст ошибки: ', partp_errnp)

    print(
        " введено значение, не отличающееся от того, что введенов поле'пароль', если тест будет провален, система выведет ошибку")

    NParol = pytest.driver.find_element(By.CSS_SELECTOR, 'input#password-confirm')
    time.sleep(1)
    NParol.send_keys(Keys.CONTROL + "A")
    NParol.send_keys(Keys.BACKSPACE)
    NParol.send_keys(PrL_V)
    but_reg = pytest.driver.find_element(By.CSS_SELECTOR, "section#page-right > div > div > div > form > button")
    but_reg.click()
    errnp = pytest.driver.find_elements(By.CSS_SELECTOR,  'section#page-right > div > div > div > form > div:nth-of-type(4) > div:nth-of-type(2) > span')
    for i in range(len(errnp)):
        partp_errnp = errnp[i].text.split(", ")
        print('текст ошибки: ', partp_errnp)

    print('ТЕСТИРОВАНИЕ СЦЕНАРИЯ СТРАНИЦЫ РЕГИСТРАЦИИ ЗАВЕРШЕНО')