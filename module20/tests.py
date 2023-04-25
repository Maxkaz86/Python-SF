from datetime import datetime

import pytest
import requests

from decorators import do_twice


#
# def my_decorator(func):
#     def wrapper():
#         print("Начало выполнения функции.")
#         func()
#         print("Конец выполнения функции.")
#
#     return wrapper
#
#
# # Эту функцию мы будем декорировать
# def my_first_decorator():
#     print("Это мой первый декоратор!")
#
#
# my_first_decorator = my_decorator(my_first_decorator)
# my_first_decorator()
#
#
# @do_twice
# def test_twice():
#     print('Это вызов функции test_twice!')
#
# test_twice()
#
# @do_twice
# def test_twice_without_params():
#     print("Этот вызов без параметров")
#
#
# @do_twice
# def test_twice_2_params(str1, str2):
#     print("В этой функции 2 параметра - {0} и {1}".format(str1, str2))
#
# @do_twice
# def test_twice(str):
#     print("Этот вызов возвращает строку {0}".format(str))
#
# test_twice_without_params()
# test_twice_2_params("1", "2")
# test_twice("single")

# @pytest.fixture()
# def request_fixture(request):
#     print(request.fixturename)
#     print(request.scope)
#     print(request.function.__name__)
#     print(request.cls)
#     print(request.module.__name__)
#     print(request.fspath)
#     if request.cls:
#         return f"\n У теста {request.function.__name__} класс есть\n"
#     else:
#         return f"\n У теста {request.function.__name__} класса нет\n"


@pytest.fixture(scope='class')
def get_key():
    # переменные email и password нужно заменить своими учетными данными
    response = requests.post(url='https://petfriends.skillfactory.ru/login',
                             data={"email": 'max@mail.ru', "pass": 'Maksim123'})
    assert response.status_code == 200, 'Запрос выполнен неуспешно'
    assert 'Cookie' in response.request.headers, 'В запросе не передан ключ авторизации'
    print('\n return auth_key')
    return response.request.headers.get('Cookie')


@pytest.fixture(autouse=True)
def request_fixture(request):
    if 'Pets' in request.function.__name__:
        print(f"\nЗапущен тест из сьюта Дом Питомца: {request.function.__name__}")


class TestClassPets:

    def test_getAllPets2(self, get_key):
        response = requests.get(url='https://petfriends.skillfactory.ru/api/pets',
                                headers={"Cookie": get_key})
        assert response.status_code == 200, 'Запрос выполнен неуспешно'
        assert len(response.json().get('pets')) > 0, 'Количество питомцев не соответствует ожиданиям'

    def test_getMyPets2(self, get_key):
        response = requests.get(url='https://petfriends.skillfactory.ru/my_pets',
                                headers={"Cookie": get_key})
        assert response.status_code == 200, 'Запрос выполнен успешно'
        assert response.headers.get('Content-Type') == 'text/html; charset=utf-8'

    def test_anotherTest(self):
        pass


@pytest.fixture(autouse=True)
def time_delta():
    start_time = datetime.now()
    yield
    end_time = datetime.now()
    print(f"\nТест шел: {end_time - start_time}")



