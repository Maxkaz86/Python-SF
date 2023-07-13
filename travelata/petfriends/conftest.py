from datetime import datetime

import pytest
from selenium import webdriver
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

BASE_URL = 'https://petfriends.skillfactory.ru/'
USER = 'max@mail.ru'
PASSWORD = 'Maksim123'


@pytest.fixture(scope='session')
def selenium_driver(request):
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.implicitly_wait(5)
    driver.get(BASE_URL + 'login')
    driver.find_element(By.ID, 'email').send_keys(USER)
    driver.find_element(By.ID, 'pass').send_keys(PASSWORD)
    driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()

    yield driver

    driver.quit()


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    setattr(item, 'rep ' + rep.when, rep)


@pytest.fixture(scope="function", autouse=True)
def failed_check(request):
    yield
    if request.node.rep_setup.failed:
        print('test is failed', request.node.nodeid)
    elif request.node.rep_test_travelata.pysetup.passed:
        if request.node.rep_call.failed:
            driver = request.node.funcargs['selenium_driver']
            make_screenshot(driver, request.node.nodeid)
            print('executing is failed', request.node.nodeid)


def make_screenshot(driver, nodeid):
    time.sleep(1)
    file_name = f'{nodeid}_{datetime.today().strftime("%Y-%m-%d_%H:%M")}.png'.replace('/', '_').replace('::', '__')
    driver.save_screenshot(file_name)
