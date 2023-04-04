import json

import requests

params = {
    'status': 'available'
}
headers = {
    'accept': 'application/json',
    'Content-Type': 'application/json'
}
data = {
      "id": 0,
      "username": "qwer123",
      "firstName": "Dima",
      "lastName": "Dimon",
      "email": "dima@mail.ru",
      "password": "Dimon123",
      "phone": "89001231212",
      "userStatus": 0
}
user = data['username']

user_update = {
    "id": 0,
      "username": "qwer123",
      "firstName": "Dima",
      "lastName": "Miha",
      "email": "dima@mail.ru",
      "password": "Dimon123",
      "phone": "89001231212",
      "userStatus": 0
}


def get_pets_by_status():
    res = requests.get(f'https://petstore.swagger.io/v2/pet/findByStatus', headers=headers, params=params)
    status = res.status_code
    result = ''
    try:
        result = res.json()
    except:
        result = res.text
    return status, result


def add_new_pet():
    res = requests.post(f'https://petstore.swagger.io/v2/user', headers=headers, data=json.dumps(data))
    status = res.status_code
    result = ''
    try:
        result = res.json()
    except:
        result = res.text
    return status, result


def update_pet():
    res = requests.put(f'https://petstore.swagger.io/v2/user/{user}', data=json.dumps(user_update), headers=headers)
    status = res.status_code
    result = ''
    try:
        result = res.json()
    except:
        result = res.text
    return status, result


def delete_pet():
    res = requests.delete(f'https://petstore.swagger.io/v2/user/{user}', headers=headers)
    status = res.status_code
    result = ''
    try:
        result = res.json()
    except:
        result = res.text
    return status, result


print(get_pets_by_status())
print(add_new_pet())
print(update_pet())
print(delete_pet())