from selenium import webdriver

from Pages.auth_page import AuthPage

driver = webdriver.Chrome()

def test_auth_page_correct():
    page = AuthPage(driver)
    page.enter_email('max@mail.ru')
    page.enter_password('Maksim123')
    page.push_button()
    assert page.get_relative_link() == '/all_pets'
