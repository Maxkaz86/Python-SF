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

res = requests.get(f'https://petstore.swagger.io/v2/pet/findByStatus', headers=headers, params=params)
res1 = requests.post(f'https://petstore.swagger.io/v2/user', headers=headers, data=json.dumps(data))
res2 = requests.put(f'https://petstore.swagger.io/v2/user/{user}', data=json.dumps(user_update), headers=headers)
res3 = requests.delete(f'https://petstore.swagger.io/v2/user/{user}', headers=headers)

print(res.status_code)
print(res.json())
print(res1.status_code)
print(res1.json())
print(res2.status_code)
print(res2.json())
print(res3.status_code)
print(res3.json())
