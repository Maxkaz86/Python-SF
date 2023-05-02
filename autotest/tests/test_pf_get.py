from datetime import datetime
import pytest
from api import PetFriends
import os
from settings import valid_email, valid_password, non_valid_email, non_valid_password

pf = PetFriends()


def generate_string(n):
    return 'x' * n


def russian_chars():
    return 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'


# Здесь мы взяли 20 популярных китайских иероглифов
def chinese_chars():
    return '的一是不了人我在有他这为之大来以个中上们'


def special_chars():
    return '|\\/!@#$%^&*()-_=+`~?"№;:[]{}'


@pytest.fixture(scope='class')
def get_api_key(email=valid_email, password=valid_password):
    """ Проверяем что запрос api ключа возвращает статус 200 и в тезультате содержится слово key"""

    # Отправляем запрос и сохраняем полученный ответ с кодом статуса в status, а текст ответа в result
    status, result = pf.get_api_key(email, password)

    # сверяем полученные данные с нашими ожиданиями
    # assert status == 200
    # assert 'key' in result
    return result


class TestPetFriends:

    @pytest.mark.api
    @pytest.mark.parametrize('filter', [generate_string(255), generate_string(1000),
                                        russian_chars(),
                                        russian_chars().upper(),
                                        chinese_chars(),
                                        special_chars(),
                                        123],
                             ids=['255 symbols', '1000 symbols',
                                  'russian',
                                  'RUSSIAN',
                                  'chinese',
                                  'specials',
                                  'digits'])
    def test_get_all_pets_with_negative_filter(self, filter, get_api_key):
        """ Проверяем что запрос всех питомцев возвращает не пустой список.
        Для этого сначала получаем api ключ и сохраняем в переменную auth_key. Далее используя этого ключ
        запрашиваем список всех питомцев и проверяем что список не пустой.
        Доступное значение параметра filter - 'my_pets' либо '' """

        # _, auth_key = pf.get_api_key(valid_email, valid_password)
        status, result = pf.get_list_of_pets(get_api_key, filter)

        assert status == 500

    @pytest.mark.api
    @pytest.mark.parametrize('filter', ['my_pets', ''],
                             ids=['only my pets', 'empty'])
    def test_get_all_pets_with_valid_filter(self, filter, get_api_key):
        """ Проверяем что запрос всех питомцев возвращает не пустой список.
        Для этого сначала получаем api ключ и сохраняем в переменную auth_key. Далее используя этого ключ
        запрашиваем список всех питомцев и проверяем что список не пустой.
        Доступное значение параметра filter - 'my_pets' либо '' """

        # _, auth_key = pf.get_api_key(valid_email, valid_password)
        status, result = pf.get_list_of_pets(get_api_key, filter)

        assert status == 200
        assert len(result['pets']) > 0
