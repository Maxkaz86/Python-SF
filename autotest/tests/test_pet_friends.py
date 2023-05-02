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


# def is_age_valid(age):
#     # Проверяем, что возраст - это число от 1 до 49 и целое
#     return age.isdigit() and 0 < int(age) < 50 and float(age) == int(age)


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

    def test_get_api_key(self, email=valid_email, password=valid_password):
        """ Проверяем что запрос api ключа возвращает статус 200 и в тезультате содержится слово key"""

        # Отправляем запрос и сохраняем полученный ответ с кодом статуса в status, а текст ответа в result
        status, result = pf.get_api_key(email, password)

        # сверяем полученные данные с нашими ожиданиями
        assert status == 200
        assert 'key' in result
        assert 'content-type' in result['body']


    @pytest.mark.add
    @pytest.mark.api
    def test_add_new_pet_with_valid_data(self, get_api_key, name='Кураж', animal_type='британец',
                                         age='8', pet_photo='images/amer.jpg'):
        """Проверяем что можно добавить питомца с корректными данными"""

        # Получаем полный путь изображения питомца и сохраняем в переменную pet_photo
        pet_photo = os.path.join(os.path.dirname(__file__), pet_photo)

        # Запрашиваем ключ api и сохраняем в переменую auth_key
        # _, auth_key = pf.get_api_key(valid_email, valid_password)

        # Добавляем питомца
        status, result = pf.add_new_pet(get_api_key, name, animal_type, age, pet_photo)

        # Сверяем полученный ответ с ожидаемым результатом
        assert status == 200
        assert result['name'] == name

    @pytest.mark.update
    @pytest.mark.api
    def test_successful_update_self_pet_info(self, get_api_key, name='Мурзик', animal_type='сфинкс', age='5'):
        """Проверяем возможность обновления информации о питомце"""

        # Получаем ключ auth_key и список своих питомцев
        # _, auth_key = pf.get_api_key(valid_email, valid_password)
        _, my_pets = pf.get_list_of_pets(get_api_key, "my_pets")

        # Еслди список не пустой, то пробуем обновить его имя, тип и возраст
        if len(my_pets['pets']) > 0:
            status, result = pf.update_pet_info(get_api_key, my_pets['pets'][0]['id'], name, animal_type, age)

            # Проверяем что статус ответа = 200 и имя питомца соответствует заданному
            assert status == 200
            assert result['name'] == name
        else:
            # если спиок питомцев пустой, то выкидываем исключение с текстом об отсутствии своих питомцев
            raise Exception("There is no my pets")

    @pytest.mark.api
    def test_successful_delete_self_pet(self, get_api_key):
        """Проверяем возможность удаления питомца"""

        # Получаем ключ auth_key и запрашиваем список своих питомцев
        # _, auth_key = pf.get_api_key(valid_email, valid_password)
        _, my_pets = pf.get_list_of_pets(get_api_key, "my_pets")

        # Проверяем - если список своих питомцев пустой, то добавляем нового и опять запрашиваем список своих питомцев
        if len(my_pets['pets']) == 0:
            pf.add_new_pet(get_api_key, "Суперкот", "кот", '3', "images/amer.jpg")
            _, my_pets = pf.get_list_of_pets(get_api_key, "my_pets")

        # Берём id первого питомца из списка и отправляем запрос на удаление
        pet_id = my_pets['pets'][0]['id']
        status, _ = pf.delete_pet(get_api_key, pet_id)

        # Ещё раз запрашиваем список своих питомцев
        _, my_pets = pf.get_list_of_pets(get_api_key, "my_pets")

        # Проверяем что статус ответа равен 200 и в списке питомцев нет id удалённого питомца
        assert status == 200
        assert pet_id not in my_pets.values()

    @pytest.mark.auth
    @pytest.mark.api
    def test_non_valid_login(self, email=non_valid_email, password=valid_password):
        """ Проверяем что запрос api ключа возвращает статус 403 и в тезультате содержится ответ,
        что пользователь с таким именем не найден"""

        # Отправляем запрос и сохраняем полученный ответ с кодом статуса в status, а текст ответа в result
        status, result = pf.get_api_key(email, password)

        # сверяем полученные данные с нашими ожиданиями
        assert status == 403
        assert 'key' not in result

    @pytest.mark.auth
    @pytest.mark.api
    def test_non_valid_password(self, email=valid_email, password=non_valid_password):
        """ Проверяем что запрос api ключа возвращает статус 403 и в тезультате содержится ответ,
        что пользователь с таким паролем не найден"""

        # Отправляем запрос и сохраняем полученный ответ с кодом статуса в status, а текст ответа в result
        status, result = pf.get_api_key(email, password)

        # сверяем полученные данные с нашими ожиданиями
        assert status == 403
        assert 'key' not in result

    @pytest.mark.update
    @pytest.mark.api
    def test_successful_update_pet_info_no_type(self, get_api_key, name='Мурзик', animal_type='', age='5'):
        """Проверяем возможность обновления информации о питомце без указания типа питомца
        и тип питомца должен остаться без изменений"""

        # Получаем ключ auth_key и список своих питомцев
        # _, auth_key = pf.get_api_key(valid_email, valid_password)
        _, my_pets = pf.get_list_of_pets(get_api_key, "my_pets")

        # Еслди список не пустой, то пробуем обновить его имя, тип и возраст
        if len(my_pets['pets']) > 0:
            status, result = pf.update_pet_info(get_api_key, my_pets['pets'][0]['id'], name, animal_type, age)
            _, r = pf.get_list_of_pets(get_api_key, filter='my_pets')

            # Проверяем что статус ответа = 200 и тип питомца не изменился
            assert status == 200
            assert result['animal_type'] == r['pets'][0]['animal_type']
        else:
            # если спиок питомцев пустой, то выкидываем исключение с текстом об отсутствии своих питомцев
            raise Exception("There is no my pets")

    @pytest.mark.update
    @pytest.mark.api
    def test_successful_update_pet_info_no_age(self, get_api_key, name='Мурзик', animal_type='кот', age=''):
        """Проверяем возможность обновления информации о питомце без указания возраста питомца
        и возраст питомца должен остаться без изменений"""

        # Получаем ключ auth_key и список своих питомцев
        # _, auth_key = pf.get_api_key(valid_email, valid_password)
        _, my_pets = pf.get_list_of_pets(get_api_key, "my_pets")

        # Еслди список не пустой, то пробуем обновить его имя, тип и возраст
        if len(my_pets['pets']) > 0:
            status, result = pf.update_pet_info(get_api_key, my_pets['pets'][0]['id'], name, animal_type, age)
            _, r = pf.get_list_of_pets(get_api_key, filter='my_pets')

            # Проверяем что статус ответа = 200 и возраст питомца не изменился
            assert status == 200
            assert result['age'] == r['pets'][0]['age']
        else:
            # если спиок питомцев пустой, то выкидываем исключение с текстом об отсутствии своих питомцев
            raise Exception("There is no my pets")

    @pytest.mark.skip(reason='API работает некорректно')
    def test_update_pet_info_just_space_name(self, get_api_key, name=' ', animal_type='кот', age='2'):
        """Отправка запроса на обновления данных, указав в имени пробел
        проверяем проверку введенных данных. на данный момент тест не проходит,
        так как API принимает символ пробела для поля имя"""

        # Получаем ключ auth_key и список своих питомцев
        # _, auth_key = pf.get_api_key(valid_email, valid_password)
        _, my_pets = pf.get_list_of_pets(get_api_key, "my_pets")

        # Еслди список не пустой, то пробуем обновить его имя, тип и возраст
        if len(my_pets['pets']) > 0:
            status, result = pf.update_pet_info(get_api_key, my_pets['pets'][0]['id'], name, animal_type, age)
            _, r = pf.get_list_of_pets(get_api_key, filter='my_pets')

            # Проверяем что статус ответа = 400
            assert status == 400
        else:
            # если спиок питомцев пустой, то выкидываем исключение с текстом об отсутствии своих питомцев
            raise Exception("There is no my pets")

    @pytest.mark.skip(reason='API работает некорректно')
    def test_update_pet_info_just_space_type(self, get_api_key, name='Джек', animal_type=' ', age='2'):
        """Отправка запроса на обновления данных, указав в типе животного пробел
        проверяем проверку введенных данных. на данный момент тест не проходит,
        так как API принимает символ пробела для поля тип животного"""

        # Получаем ключ auth_key и список своих питомцев
        # _, auth_key = pf.get_api_key(valid_email, valid_password)
        _, my_pets = pf.get_list_of_pets(get_api_key, "my_pets")

        # Еслди список не пустой, то пробуем обновить его имя, тип и возраст
        if len(my_pets['pets']) > 0:
            status, result = pf.update_pet_info(get_api_key, my_pets['pets'][0]['id'], name, animal_type, age)
            _, r = pf.get_list_of_pets(get_api_key, filter='my_pets')

            # Проверяем что статус ответа = 400
            assert status == 400
        else:
            # если спиок питомцев пустой, то выкидываем исключение с текстом об отсутствии своих питомцев
            raise Exception("There is no my pets")

    @pytest.mark.add
    @pytest.mark.api
    @pytest.mark.parametrize("name", [''], ids=['empty'])
    @pytest.mark.parametrize("animal_type", [''], ids=['empty'])
    @pytest.mark.parametrize("age", ['', '-1', '0', '100', '1.5',
                                     '2147483647',
                                     '2147483648',
                                     russian_chars(),
                                     russian_chars().upper(),
                                     chinese_chars(),
                                     special_chars()], ids=['empty',
                                                            'negative',
                                                            'zero',
                                                            'number 100',
                                                            'float',
                                                            'huge number',
                                                            'huge number',
                                                            'russian',
                                                            'RUSSIAN',
                                                            'chinese',
                                                            'specials'])
    def test_add_pet_un_photo(self, get_api_key, name, animal_type, age):
        """Проверяем что можно добавить питомца с корректными данными без фото.
        Тест не проходит, так как API пропускает пустое значение параметра"""

        # Запрашиваем ключ api и сохраняем в переменую auth_key
        # _, auth_key = pf.get_api_key(valid_email, valid_password)

        # Добавляем питомца
        status, result = pf.add_new_pet_no_photo(get_api_key, name, animal_type, age)

        # Сверяем полученный ответ с ожидаемым результатом
        assert status == 400

    @pytest.mark.add
    @pytest.mark.api
    @pytest.mark.parametrize("name", [generate_string(255), generate_string(1001),
                                      russian_chars(),
                                      russian_chars().upper(),
                                      chinese_chars(),
                                      special_chars(),
                                      '123'], ids=['255 symbols',
                                                   'more than 1000 symbols',
                                                   'russian',
                                                   'RUSSIAN',
                                                   'chinese',
                                                   'specials',
                                                   'digit'])
    @pytest.mark.parametrize("animal_type", [generate_string(255), generate_string(1001),
                                             russian_chars(),
                                             russian_chars().upper(),
                                             chinese_chars(),
                                             special_chars(),
                                             '123'], ids=['255 symbols',
                                                          'more than 1000 symbols',
                                                          'russian',
                                                          'RUSSIAN',
                                                          'chinese',
                                                          'specials',
                                                          'digit'])
    @pytest.mark.parametrize("age", ['1'], ids=['min'])
    def test_add_pet_un_photo(self, get_api_key, name, animal_type, age):
        """Проверяем что можно добавить питомца с корректными данными без фото.
        Тест не проходит, так как API пропускает пустое значение параметра"""

        # Запрашиваем ключ api и сохраняем в переменую auth_key
        # _, auth_key = pf.get_api_key(valid_email, valid_password)

        # Добавляем питомца
        status, result = pf.add_new_pet_no_photo(get_api_key, name, animal_type, age)

        # Сверяем полученный ответ с ожидаемым результатом
        assert status == 200
        assert result['name'] == name
        assert result['age'] == age
        assert result['animal_type'] == animal_type

    @pytest.mark.add
    @pytest.mark.api
    def test_add_photo_exist_pet(self, get_api_key, pet_photo='images/307.jpg'):
        """Проверяем что можно добавить фото питомца к уже существующему животному в базе данных
         для этого отправляем запрос надобавление фотографии и получаем в ответ код 200 о том что операция выполнена
         и проверяем, что в ответе параметр фото не пуст"""
        # Получаем полный путь изображения питомца и сохраняем в переменную pet_photo
        pet_photo = os.path.join(os.path.dirname(__file__), pet_photo)

        # Получаем ключ auth_key и список своих питомцев
        # _, auth_key = pf.get_api_key(valid_email, valid_password)
        _, my_pets = pf.get_list_of_pets(get_api_key, "my_pets")

        status, result = pf.add_photo_for_pet(get_api_key, my_pets['pets'][0]['id'], pet_photo)

        assert status == 200
        assert result['pet_photo'] != ''

    @pytest.mark.skip(reason='API работает некорректно')
    def test_add_pet_incorrect_name(self, get_api_key, name='%!$', animal_type='Собака', age='4'):
        """Отправляем запрос, чтобы добавить питомца без фото с именем в виде спецсимволов
        ожидаем ответ от сервера, что формат имени некорректный и ошибку 400
        на данный момент тест проваливается, так как api пропускает спецсимволы в имени"""

        # Запрашиваем ключ api и сохраняем в переменую auth_key
        # _, auth_key = pf.get_api_key(valid_email, valid_password)

        # Добавляем питомца
        status, _ = pf.add_new_pet_no_photo(get_api_key, name, animal_type, age)

        # Сверяем полученный статус
        assert status == 400

    @pytest.mark.xfail(reason='API работает некорректно')
    def test_add_pet_incorrect_type(self, get_api_key, name='Луна', animal_type='$%!', age='4'):
        """Отправляем запрос, чтобы добавить питомца без фото, тип животного указан в виде спецсимволов
        ожидаем ответ от сервера, что формат имени некорректный и ошибку 400
        на данный момент тест проваливается, так как api пропускает спецсимволы в типе животного"""

        # Запрашиваем ключ api и сохраняем в переменую auth_key
        # _, auth_key = pf.get_api_key(valid_email, valid_password)

        # Добавляем питомца
        status, _ = pf.add_new_pet_no_photo(get_api_key, name, animal_type, age)

        # Сверяем полученный статус
        assert status == 400


@pytest.fixture(autouse=True)
def time_delta():
    start_time = datetime.now()
    yield
    end_time = datetime.now()
    print(f"\n Тест шел: {end_time - start_time}")
