import time


from .locators import AuthLocators
from .base_page import BasePage
import os


class AuthPage(BasePage):
    def __init__(self, driver, timeout=10):
        # Тут мы обращаемся к методу __init__ нашего родительского класса BasePage,
        # так как наш новый метод __init__ затрёт его
        super().__init__(driver, timeout)
        url = os.getenv("login_url") or "https://petfriends.skillfactory.ru/login"
        driver.get(url)
        # создаем нужные элементы
        self.email = driver.find_element(*AuthLocators.AUTH_EMAIL)
        self.password = driver.find_element(*AuthLocators.AUTH_PASS)
        self.btn = driver.find_element(*AuthLocators.AUTH_BTN)
        time.sleep(3)

    def enter_email(self, value):
        self.email.send_keys(value)

    def enter_password(self, value):
        self.password.send_keys(value)

    def push_button(self):
        self.btn.click()

    time.sleep(3)
