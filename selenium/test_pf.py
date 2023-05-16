import time
from selenium.webdriver.common.by import By


def test_petfriends(web_browser):
    # Open PetFriends base page:
    web_browser.get("https://petfriends.skillfactory.ru/")

    time.sleep(5)  # just for demo purposes, do NOT repeat it on real projects!

    # click on the new user button
    btn_newuser = web_browser.find_element(By.XPATH, "//button[@onclick=\"document.location='/new_user';\"]")
    btn_newuser.click()

    # click existing user button
    btn_exist_acc = web_browser.find_element(By.PARTIAL_LINK_TEXT, "У меня уже есть аккаунт")
    btn_exist_acc.click()

    # add email
    field_email = web_browser.find_element(By.ID, "email")
    field_email.clear()
    field_email.send_keys("max@mail.ru")

    # add password
    field_pass = web_browser.find_element(By.ID, "pass")
    field_pass.clear()
    field_pass.send_keys("Maksim123")

    # click submit button
    btn_submit = web_browser.find_element(By.XPATH, "//button[@type='submit']")
    btn_submit.click()

    time.sleep(5)  # just for demo purposes, do NOT repeat it on real projects!

    assert web_browser.current_url == 'https://petfriends.skillfactory.ru/all_pets', "login error"
