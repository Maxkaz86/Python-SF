import pytest
import time
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from data import Pr20, numb, PrL_V, ML

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

    print('ТЕСТИРОВАНИЕ СЦЕНАРИЯ АВТОРИЗАЦИИ')
    avt_r = pytest.driver.find_elements(By.ID, 'page-right')
    for i in range(len(avt_r)):
        parts_rr = avt_r[i].text.split(", ")
        print('правая часть содержит: ', parts_rr)

    avt_l = pytest.driver.find_elements(By.ID, 'page-left')
    for i in range(len(avt_l)):
        parts_rl = avt_l[i].text.split(", ")
        print('левая часть содержит: ', parts_rl)

    time.sleep(2)

    print('                    Тестирование строк во вкладке "номер":')

    tpar = pytest.driver.find_element(By.CSS_SELECTOR, 'input#username')
    time.sleep(1)
    tpar.send_keys(Keys.CONTROL + "A")
    tpar.send_keys(Keys.BACKSPACE)
    tpar.send_keys(numb)
    tpar.send_keys(Keys.TAB)


    print('                    Проверка при вводе валидных значений в поле "пароль":')
    print('    Произведены 2 теста с валидными и невалидным паролями. Если какой-либо тест будет провален, система выдаст ошибку ')

    Parol = pytest.driver.find_element(By.CSS_SELECTOR, 'input#password')
    time.sleep(1)
    Parol.send_keys(Keys.CONTROL + "A")
    Parol.send_keys(Keys.BACKSPACE)
    Parol.send_keys(Pr20)
    but_autn = pytest.driver.find_element(By.CSS_SELECTOR, 'button#kc-login')
    but_autn.click()
    errp = pytest.driver.find_elements(By.CSS_SELECTOR,'span#form-error-message')
    for i in range(len(errp)):
        partp_errp = errp[i].text.split(", ")
        print('текст ошибки при вводе 20 латинских букв: ', partp_errp)

    Parol = pytest.driver.find_element(By.CSS_SELECTOR, 'input#password')
    time.sleep(1)
    Parol.send_keys(Keys.CONTROL + "A")
    Parol.send_keys(Keys.BACKSPACE)
    Parol.send_keys(PrL_V)
    but_autn = pytest.driver.find_element(By.CSS_SELECTOR, 'button#kc-login')
    but_autn.click()
    errp = pytest.driver.find_elements(By.CSS_SELECTOR, 'span#form-error-message')
    for i in range(len(errp)):
        partp_errp = errp[i].text.split(", ")
        print('текст ошибки при вводе верного пароля: ', partp_errp)

    print('      Сценарий авторизации клиента на вкладке "почта"  ')

    pytest.driver.find_element(By.CSS_SELECTOR, 'div#t-btn-tab-mail').click()
    EM = pytest.driver.find_element(By.CSS_SELECTOR, 'input#username')
    time.sleep(1)
    EM.send_keys(Keys.CONTROL + "A")
    EM.send_keys(Keys.BACKSPACE)
    EM.send_keys(ML)
    EM.send_keys(Keys.TAB)

    print('                    Проверка при вводе валидных значений в поле "пароль":')
    print('    Произведены 2 теста с валидными и невалидным паролями. Если какой-либо тест будет провален, система выдаст ошибку ')

    ParoEl = pytest.driver.find_element(By.CSS_SELECTOR, 'input#password')
    time.sleep(1)
    ParoEl.send_keys(Keys.CONTROL + "A")
    ParoEl.send_keys(Keys.BACKSPACE)
    ParoEl.send_keys(Pr20)
    but_autn_El = pytest.driver.find_element(By.CSS_SELECTOR, 'button#kc-login')
    but_autn_El.click()
    errel = pytest.driver.find_elements(By.CSS_SELECTOR, 'section#page-right > div > div > div > form > div > div:nth-of-type(2) > span')
    for i in range(len(errel)):
        partp_errel = errel[i].text.split(", ")
        print('текст ошибки при вводе 20 латинских букв: ', partp_errel)

    ParoEl = pytest.driver.find_element(By.CSS_SELECTOR, 'input#password')
    time.sleep(1)
    ParoEl.send_keys(Keys.CONTROL + "A")
    ParoEl.send_keys(Keys.BACKSPACE)
    ParoEl.send_keys(PrL_V)
    but_autn_El = pytest.driver.find_element(By.CSS_SELECTOR, 'button#kc-login')
    but_autn_El.click()
    errel = pytest.driver.find_elements(By.CSS_SELECTOR,'section#page-right > div > div > div > form > div > div:nth-of-type(2) > span')
    for i in range(len(errel)):
        partp_errel = errel[i].text.split(", ")
        print('текст ошибки при вводе верного пароля:  ', partp_errel)