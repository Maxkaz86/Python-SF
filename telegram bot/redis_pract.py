import redis
import json

red = redis.Redis(
    host='redis-15647.c83.us-east-1-2.ec2.cloud.redislabs.com',
    port=15647,
    password='rpgeKIENf6SSedBYpEAkKu57lFKET6dU'
)

# dict1 = {'var1': 'value1', 'var2': 'value2'}
# red.set('dict1', json.dumps(dict1)) # с помощью функции dumps() из модуля json превратим наш словарь в строчку
# converted_dict = json.loads(red.get('dict1')) # с помощью знакомой нам функции превращаем данные полученные из кэша обратно в словарь
#
# print(type(converted_dict))
# print(converted_dict)

# red.delete('dict1') # удаляются ключи с помощью метода .delete()
# print(red.get('dict1'))