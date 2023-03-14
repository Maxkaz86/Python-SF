# string = '{1}, {2}, {0}'.format('Ivan', 'Petya', 'Katya')
# print(string)
# empty_m = []
# numbers = [10,12,122,11]
# amount = int(input('введите число '))
# for n in numbers:
#     empty_m.append(amount * n)
# print(empty_m)
# a = [
#     1,2,3,
#     4,5
# ]
# print(a)
# def is_leap_year(x):
#     return x % 400 == 0 or ((x % 4 == 0) and (x % 100 != 0))
# print(is_leap_year(x = 3000))
# try:
#     a = int(input("введите число:\t"))
# except ValueError as e:
#     print("Вы ввели не правильное число")
# else:
#     print(f'Вы ввели число {a}')
# finally:
#     print("выход из программы")
# speed = int(input('укажите скорость ветра: '))
# def get_wind_class(speed):
#     if speed in [1, 2, 3, 4]:
#         return "weak [1]"
#     elif 5 <= speed <= 10:
#         return 'moderate [2]'
#     elif 11 <= speed <= 18:
#         return 'strong [3]'
#     elif speed >= 19:
#         return 'hurricane [4]'
# A = int(input('write num '))
# B = int(input('write num '))
# C = int(input('write num '))
# if A < 45 and B >= 45 and C >= 45:
#     print('true')
# elif A >= 45 and B < 45 and C >= 45:
#     print('true')
# elif A >= 45 and B >= 45 and C < 45:
#     print('true')
# else:
#     print("False")
# if A > 15 or A < -10 or -1 < A < 2:
# if not (-10 <= A <= -1 or 2 <= A <= 15):
#     print('All is ok')
# else:
#     print('False')
# if A % 5 == 0 and A // 5 not in [2,4,6,8,12,14,16,18]:
#     print('число содержит 5')
# else:
#     print('число 5 не входит')
# if 5 in list(map(int, list(str(A)))):
#     print('it has number 5')
# else:
#     print("It's not has number 5")
# list_ = [-5, 2, 4, 8, 12, -7, 5]
# print(len(list_) == len(set(list_))) преобразует список таким образом, что повторяющиеся значения объединяются
# a = 12344321
# print(str(a) == str(a)[::-1])
# s = 1
# while True:
#     s += 1
#     if s ** 2 >= 1000:
#         break
# print(s - 1)
# n = 4
# s = 6
# matrix = [
#     [1,2,3,4,5,6],
#     [7,8,9,10,11,12],
#     [13,2,3,4,5,6],
#     [8,7,6,5,4,3]
# ]
# for i in range(4):
#     for j in range(6):
#         print(matrix[i][j], end=' ')
#     print()
import numpy

# random_matrix = [
#     [9, 2, 1],
#     [2, 5, 3],
#     [4, 8, 5]
# ]
#
# min_value_rows = []  # здесь будут храниться минимальные значения для каждой строки
# min_index_rows = []  # здесь будут храниться индексы минимальных значений для каждой строки
# max_value_rows = []  # здесь будут храниться максимальные значения для каждой строки
# max_index_rows = []  # здесь будут храниться индексы максимальных значений для каждой строки
#
# for row in random_matrix:  # здесь мы целиком берем каждую сроку
#     min_index = 0  # в качестве минимального значения возьмем первый элемент строки
#     max_index = 0
#     min_value = row[min_index]  # начальное минимальное значение для каждой строки будет новое
#     max_value = row[max_index]  # для максимального значения тоже самое
#      for index_col in range(len(row)):
#          if row[index_col] < min_value:
#              min_value = row[index_col]
#              min_index = index_col
#          if row[index_col] > max_value:
#              max_value = row[index_col]
#              max_index = index_col
#      min_value_rows.append(min_value)
#      min_index_rows.append(min_index)
#      max_value_rows.append(max_value)
#      max_index_rows.append(max_index)
#
#  print(min_value_rows)
#  print(min_index_rows)
#  print(max_value_rows)
#  print(max_index_rows)

# list_ = [-5, 2, 4, 8, 12, -7, 5]
# # Объявим переменную, в которой будем хранить индекс отрицательного элемента
# index_negative = None
# for i, value in enumerate(list_):
#     if value < 0:
#         print("Отрицательное число: ", value)
#         index_negative = i  # перезаписываем значение индекса
#         print("Новый индекс отрицательного числа: ", index_negative)
#     else:
#         print("Положительное число: ", value)
#     print("---")
# print("Конец цикла")
# print()
# print("Ответ: индекс последнего отрицательного элемента = ", index_negative)

# list_ = [-5, 2, 4, 8, 12, -7, 5]
# # Функция enumerate возвращает данные в виде кортежей,
# # где на первом месте стоит индекс, а затем значение
# # [(0, -5), (1, 2), (2, 4), ...]
# for i, value in enumerate(list_):
#     print("Индекс элемента: ", i)
#     print("Значение элемента: ", value)  # с помощью индекса получаем значение элемента
#     print("---")
# print("Конец цикла")

# text = """
# У лукоморья дуб зелёный;
# Златая цепь на дубе том:
# И днём и ночью кот учёный
# Всё ходит по цепи кругом;
# Идёт направо -- песнь заводит,
# Налево -- сказку говорит.
# Там чудеса: там леший бродит,
# Русалка на ветвях сидит;
# Там на неведомых дорожках
# Следы невиданных зверей;
# Избушка там на курьих ножках
# Стоит без окон, без дверей;
# Там лес и дол видений полны;
# Там о заре прихлынут волны
# На брег песчаный и пустой,
# И тридцать витязей прекрасных
# Чредой из вод выходят ясных,
# И с ними дядька их морской;
# Там королевич мимоходом
# Пленяет грозного царя;
# Там в облаках перед народом
# Через леса, через моря
# Колдун несёт богатыря;
# В темнице там царевна тужит,
# А бурый волк ей верно служит;
# Там ступа с Бабою Ягой
# Идёт, бредёт сама собой,
# Там царь Кащей над златом чахнет;
# Там русский дух... там Русью пахнет!
# И там я был, и мёд я пил;
# У моря видел дуб зелёный;
# Под ним сидел, и кот учёный
# Свои мне сказки говорил.
# """
# text = text.lower()
# text = text.replace(" ", "")
# text = text.replace("\n", "")
# count = {}  # для подсчета символов и их количества
# for char in text:
#    if char in count:  # если символ уже встречался, то увеличиваем его количество на 1
#        count[char] += 1
#    else:
#        count[char] = 1
# for char, cnt in count.items():
#    print(f"Символ {char} встречается {cnt} раз")

# n = int(input("Введите число\n"))
# while n > 1:
#     if n % 2 == 0:
#         n = n // 2
#     else:
#         n = (n * 3 + 1) // 2
#     print(n)
#     if n == 1:
#         print("Done")
#         break

# heads = 35  # количество голов
# legs = 94  # количество ног
#
# for r in range(heads + 1):  # количество кроликов
#     for ph in range(heads + 1):  # количество фазанов
#         #  если суммарное количество голов превышено или ног превышено, то переходим на следующий шаг цикла
#         if (r + ph) > heads or \
#             (r * 4 + ph * 2) > legs:
#             continue
#         if (r + ph) == heads and (r * 4 + ph * 2) == legs:
#             print("Количество кроликов", r)
#             print("Количество фазанов", ph)
#             print("---")

# a = list(map(int, input('введите последовательность чисел ')))
# print(not any(a))

# num = [[i * j for j in range(1, 11)] for i in range(1, 11)]
# print(num, sep='\n') умножение от 1 до 10

# L = [int(input('число ')) % 2 == 0 for i in range(5)]
# print(not all(L) and any(L))

# L = [i for i in range(10)]
# M = [i for i in range(10,0,-1)]
# N = [a * b for a, b in zip(L, M)]
# print(N)

# text = input()  # получаем строку
#
# first = text[0]  # сохраняем первый символ
# count = 0  # заводим счетчик
# result = ''  # и результирующую строку
#
# for c in text:
#     if c == first:  # если символ совпадает с сохраненным,
#         count += 1  # то увеличиваем счетчик
#     else:
#         result += first + str(count)  # иначе - записываем в результат
#         first = c  # и обновляем сохраненный символ с его счетчиком
#         count = 1
#
# result += first + str(count)  # и добавляем в результат последний символ
# print(result)
# letter = input('write word')
# L = ['a','e','i','u','o']
# if letter in L:
#     print('гласная')
# elif letter == 'y':
#     print('согласная и гласная')
# else:
#     print('согласная')
# a = ['отбивная','пельмени','рис','рыба']
# for i in a:
#     if i == 'пельмени':
#         print('я не ем перльмени')
#         continue
#     print('очень вкусная ' + i)
# else:
#     print('ненавижу пельмени')
# print('ужин окончен')
# def hello_world():
#     print('Hello World')
# hello_world()
# def char_frequency(text):
#    text = text.lower()
#    text = text.replace(" ", "")
#    text = text.replace("\n", "")
#
#    count = {}  # для подсчета символов и их количества
#    for char in text:
#        if char in count:  # если символ уже встречался, то увеличиваем его количество на 1
#            count[char] += 1
#        else:
#            count[char] = 1
#    print(count)
#    for char, cnt in count.items():
#        print(f"Символ {char} встречается {cnt} раз")
# char_frequency()
# def divider(a, n):
#     if a % n == 0:
#         print(f'Число {n} является делителем числа {a}')
#     else:
#         print(f'число {n} не является делителем числа {a}')
# divider(10, 3)
# def stairs(n):
#     for i in range(n, 0, -1):
#         print('*' * i)
# stairs(3)
# def divider(a):
#     count = 0
#     for n in range(1, a + 1):
#         if a % n == 0:
#             count += 1
#     return count
# print(divider(5))
# def polydron(text):
#     text = text.lower()
#     text = text.replace(' ', '')
#     if text == text[::-1]:
#         return True
#     else:
#         return False
# print(polydron("Тест"))

#
# def get_mul_func(m):
#     nonlocal_m = m
#
#     def local_mul(n):
#         return n * nonlocal_m
#
#     return local_mul
#
#
# two_mul = get_mul_func(2)  # возвращаем функцию, которая будет умножать числа на 2
# print(two_mul(5))

# def rec_fibb(n):
#    if n == 1:
#        return 0
#    if n == 2:
#       return 1
#    return rec_fibb(n - 1) + rec_fibb(n - 2)
#
# print(rec_fibb(5))
# def fact(n):
#     if n == 1:
#         return 1
#     return n + fact(n - 1)
# print(fact(3))
# def strings(n):
#     if len(n) == 0:
#         return ''
#     else:
#         return n[-1] + strings(n[:-1])
# print(strings('test'))
# def sum_digit(n):
#    if n < 10:
#        return n
#    else:
#        return n % 10 + sum_digit(n // 10)
#
# print(sum_digit(1234))
# def sum(a=1, b=1):
#     while True:
#         a += b
#         yield a
# print(sum(5,6))
# def lists(list_):
#     list_val = list_.copy()
#     while True:
#         value = list_val.pop(0)
#         list_val.append(value)
#         yield value
# for i in lists([1,2,3]):
#     print(i)
# import time
# N = 100
# def decorator_time(fn):
#    def wrapper():
#        print(f"Запустилась функция {fn}")
#        t0 = time.time()
#        result = fn()
#        dt = time.time() - t0
#        print(f"Функция выполнилась. Время: {dt:.10f}")
#        return dt  # задекорированная функция будет возвращать время работы
#    return wrapper
# def pow_2():
#    return 10000000000 ** 2
#
# def in_build_pow():
#    return pow(10000000000, 2)
#
# pow_2 = decorator_time(pow_2)
# in_build_pow = decorator_time(in_build_pow)
# mean_pow_2 = 0
# mean_in_build_pow = 0
# for i in range(N):
#     mean_pow_2 += pow_2()
#     mean_in_build_pow += in_build_pow()
# print(f'Function {pow_2} performed {N} times. Average time: {mean_pow_2/N:.10f}')
# print(f'Function {in_build_pow} performed {N} times. Average time: {mean_in_build_pow/N:.10f}')
# def my_decorator(x):
#     count = 0
#     def wrapper(*args, **kwargs):
#         nonlocal count
#         x(*args, **kwargs)
#         count += 1
#         print(f'Function {x} was called {count} times')
#     return wrapper
#
# @my_decorator
# def say_hello(word):
#     print(word)
# say_hello('Hi hi hi')
# say_hello('Something new')
# say_hello("I'm stupido")

# def cache(func):
#    cache_dict = {}
#    def wrapper(num):
#        nonlocal cache_dict
#        if num not in cache_dict:
#            cache_dict[num] = func(num)
#            print(f"Добавление результата в кэш: {cache_dict[num]}")
#        else:
#            print(f"Возвращение результата из кэша: {cache_dict[num]}")
#        print(f"Кэш {cache_dict}")
#        return cache_dict[num]
#    return wrapper
# @cache
# def f(n):
#     return n * 123456789
# f(11)
# def linier_solver(a,b):
#     if a:
#         return b/a
#     elif not a and not b:
#         return "Бесконечное количество корней"
#     else:
#         return "нет корней"
# print(linier_solver(0,0))
# def D(a,b,c):
#     return b**2 - 4*a*c
#
# def quadratic_solve(a,b,c):
#     if D(a,b,c) < 0:
#         return 'Нет вещественных корней'
#     elif D(a,b,c) == 0:
#         return -b/(2*a)
#     else:
#         return (-b - D(a, b, c) ** 0.5) / (2 * a), (-b + D(a, b, c) ** 0.5) / (2 * a)
# # D(1,3,1)
# print(quadratic_solve(1,3,1))
# task 14.5.9
# L=list(map(int,input('write numbers ').split()))
# def min_list(L):
#     if len(L) == 1:
#         return L[0]
#     return L[0] if L[0] < min_list(L[1:]) else min_list(L[1:])
# print(min_list(L))
# task 14.5.10
# def mirror(a, res=0):
#     if a == 0:
#         return res
#     else:
#         return mirror(a // 10, res * 10 + a % 10)
# def equal(N, S):
#     if S < 0:
#         return False
#     if N < 10:
#         return N == S
#     else:
#         return equal(N // 10, S - N % 10)
# print(equal(23, 5))
# def e():
#     n = 1
#
#     while True:
#         yield (1 + 1 / n) ** n
#         n += 1
# last = 0
# for a in e(): # e() - генератор
#     if (a - last) < 0.00000001: # ограничение на точность
#         print(a)
#         break # после достижения которого - завершаем цикл
#     else:
#         last = a # иначе - присваиваем новое значение
# e()
# e()
# print(a)

# USERS = ['admin', 'guest', 'director', 'root', 'superstar']
#
# yesno = input("""Введите Y, если хотите авторизоваться или N,
#              если хотите продолжить работу как анонимный пользователь: """)
#
# auth = yesno == "Y"
# def is_auth(func):
#     def wrapper():
#         if auth:
#             print("Пользователь авторизован")
#             func()
#         else:
#             print("Пользователь неавторизован. Функция выполнена не будет")
#     return wrapper
#
#
# if auth:
#     username = input("Введите ваш username:")
# def has_access(func):
#     def wrapper():
#         if username in USERS:
#             print("Авторизован как", username)
#             func()
#         else:
#             print("Доступ пользователю", username, "запрещен")
#     return wrapper
#
# @is_auth
# @has_access
# def from_db():
#     print("some data from database")
#
# from_db()
# L = ['THIS', 'IS', 'LOWER', 'STRING']
# print(list(map(str.lower, L)))
# lists = [-2, -1, 0, 1, -3, 2, -3]
# def numbers(x):
#     return x % 2 == 0
# results = list(filter(numbers, lists))
# print(results)
# data = [
#    (82, 191),
#    (68, 174),
#    (90, 189),
#    (73, 179),
#    (76, 184)
# ]
# d = min(data, key = lambda i: i[0]/i[1]**2)
# print(d)
# a = ["asd", "bbd", "ddfa", "mcsa"]

# print(list(map(lambda i: i.upper(), a)))
# print(list(map(str.upper, a)))
from datetime import datetime

# 15.1.2
# mySong = open('myfavouritesong.txt', 'rt', encoding='utf8')
# for line in mySong:
#     print(line)
# myFile = open('testfile.txt', 'w')
# myFile.write('hello')
# print('world', file = myFile)
# myFile = open('testfile.txt', 'r')
# print(myFile.read())

# alpha = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
# alphaUp = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
# number = int(input('Введите число, на которое нужно сдвинуть текст: '))
#
# summary = ''
#
#
# def changeChar(char):
#     if char in alpha:
#         return alpha[(alpha.index(char) + number) % len(alpha)]
#     elif char in alphaUp:
#         return alphaUp[(alphaUp.index(char) + number) % len(alphaUp)]
#     else:
#         return char
#
#
# with open("myfavouritesong.txt", encoding="utf8") as myFile:
#     for line in myFile:
#         for char in line:
#             summary += changeChar(char)
#
# with open("output.txt", 'w', encoding="utf8") as myFile:
#     myFile.write(summary)

# nameFile = input('Название файла: ')
# with open(nameFile, encoding='utf8') as f:
#     myFile = f.read()
#
# def changeText(text):
#     """
#     Функция принимает строку с текстом.
#     Убирает все знаки препинания и возвращает
#     список, состоящий из слов текста.
#     """
#     for i in '!"\'#$%&()*+-,/:;<=>?@[\\]^_{|}~':
#         text = text.replace(i, '')
#     return text.split()
# def mostCommon(text, length=0):
#     """
#     Функция принимает список и ограничение по длине.
#     Возвращает самый часто встречающийся элемент.
#     Если есть несколько элементов с одинаковой самой большой частотой, то вернёт их все.
#     """
#     most_common = []
#     qty_most_common = 0
#     for item in text:
#         if len(item) > length:
#             qty = text.count(item)
#             if qty > qty_most_common:
#                 qty_most_common = qty
#                 most_common = [item]
#             elif qty == qty_most_common:
#                 most_common.append(item)
#     return list(set(most_common))
#
# def mostLength(text):
#     """
#     Функция принимает список.
#     Возвращает самый длинный элемент.
#     Если есть несколько элементов с одинаковой самой большой длиной, то вернёт их все.
#     """
#     most_length = []
#     qty_most_length = 0
#     alphabet = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
#     for item in text:
#         for char in item:
#             if char not in alphabet:
#                 charEn = False
#             else:
#                 charEn = True
#         if charEn:
#             qty = len(item)
#             if qty > qty_most_length:
#                 qty_most_length = qty
#                 most_length = [item]
#             elif qty == qty_most_length:
#                 most_length.append(item)
#     return list(set(most_length))
#
# fileText = changeText(myFile)
# print(f'Список самых частых слов длинной более трёх символов: {mostCommon(fileText, 3)}')
# print(f'Список самых длинных английских слов: {mostLength(fileText)}')

# import json
# with open('file.txt', encoding='utf8') as f:
#     templates = json.load(f)
#     print(templates)
# def checkInt(item):
#     return isinstance(item, int)
# def checkStr(item):
#     return isinstance(item, str)
# def checkBool(item):
#     return isinstance(item, bool)
# def checkUrl(item):
#     if isinstance(item, str):
#         return item.startswith('http://') or item.startswith('https://')
#     else:
#         return False
# def checkStrValue(item, val):
#     if isinstance(item, str):
#         return item in val
#     else:
#         return False
# def errorLog(item, value, string):
#     error.append({item: f'{value}, {string}'})
#
# listOfItems = {
#     'timestamp': 'int',
#     'referer': 'url',
#     'location': 'url',
#     'remoteHost': 'str',
#     'partyId': 'str',
#     'sessionId': 'str',
#     'pageViewId': 'str',
#     'eventType': 'val',
#     'item_id': 'str',
#     'item_price': 'int',
#     'item_url': 'url',
#     'basket_price': 'str',
#     'detectedDuplicate': 'bool',
#     'detectedCorruption': 'bool',
#     'firstInSession': 'bool',
#     'userAgentName': 'str',
# }
# error = []
# for items in templates:
#     for item in items:
#         if item in listOfItems:
#             if listOfItems[item] == 'int':
#                 if not checkInt(items[item]):
#                     errorLog(item, items[item], f'Ожидали тип {listOfItems[item]}')
#             elif listOfItems[item] == 'str':
#                 if not checkStr(items[item]):
#                     errorLog(item, items[item], f'Ожидали тип {listOfItems[item]}')
#             elif listOfItems[item] == 'bool':
#                 if not checkBool(items[item]):
#                     errorLog(item, items[item], f'Ожидали тип {listOfItems[item]}')
#             elif listOfItems[item] == 'url':
#                 if not checkUrl(items[item]):
#                     errorLog(item, items[item], f'Ожидали тип {listOfItems[item]}')
#             elif listOfItems[item] == 'val':
#                 if not checkStrValue(items[item], ['itemBuyEvent', 'itemViewEvent']):
#                     errorLog(item, items[item], 'Ожидали значения itemBuyEvent или itemViewEvent')
#             else:
#                 errorLog(item, items[item], 'неожиданное значение')
#         else:
#             errorLog(item, items[item], 'неизвестная переменная')
#
# if error == []:
#     print('Pass')
# else:
#     print('Fail')
#     print(error)

# рекурсия
# def p(n):
#     if n == 0:
#         return
#     else:
#         p(n-1)
#         print(n)
# p(5)

# pars = {")": "(", "]": "["}
# def par_check(string):
#     stack = []
#
#     for s in string:
#         if s in "([":
#             stack.append(s)
#         elif s in ")]":
#             if len(stack) > 0 and stack[-1] == pars[s]:
#                 stack.pop()
#             else:
#                 return False
#     return len(stack) == 0
#
#
# print(par_check('((()))[]'))

# def is_empty(): # очередь пуста?
#     # да, если указатели совпадают и в них содержится ноль
#     return head == tail and queue[head] == 0
#
# def size(): # получаем размер очереди
#     if is_empty(): # если она пуста
#         return 0 # возвращаем ноль
#     elif head == tail: # иначе, если очередь не пуста, но указатели совпадают
#         return N_max # значит очередь заполнена
#     elif head > tail: # если хвост очереди сместился в начало списка
#         return N_max - head + tail
#     else: # или если хвост стоит правее начала
#         return tail - head
#
#
# def add():  # добавляем задачу в очередь
#     global tail, order
#     order += 1  # увеличиваем порядковый номер задачи
#     queue[tail] = order  # добавляем его в очередь
#     print("Задача №%d добавлена" % (queue[tail]))
#
#     # увеличиваем указатель на 1 по модулю максимального числа элементов
#     # для зацикливания очереди в списке
#     tail = (tail + 1) % N_max
#
# def show(): # выводим приоритетную задачу
#     print("Задача №%d в приоритете" % (queue[head]))
#
# def do(): # выполняем приоритетную задачу
#     global head
#     print("Задача №%d выполнена" % (queue[head]))
#     queue[head] = 0 # после выполнения зануляем элемент по указателю
#     head = (head + 1) % N_max # и циклично перемещаем указатель
#
#
# N_max = int(input("Определите размер очереди:"))
#
# queue = [0 for _ in range(10)]  # инициализируем список с нулевыми элементами
# print(queue)
# order = 0  # будем хранить сквозной номер задачи
# head = 0  # указатель на начало очереди
# tail = 0  # указатель на элемент следующий за концом очереди
#
# while True:
#     cmd = input("Введите команду:")
#     if cmd == "empty":
#         if is_empty():
#             print("Очередь пустая")
#         else:
#             print("В очереди есть задачи")
#     elif cmd == "size":
#         print("Количество задач в очереди:", size())
#     elif cmd == "add":
#         if size() != N_max:
#             add()
#         else:
#             print("Очередь переполнена")
#     elif cmd == "show":
#         if is_empty():
#             print("Очередь пустая")
#         else:
#             show()
#     elif cmd == "do":
#         if is_empty():
#             print("Очередь пустая")
#         else:
#             do()
#     elif cmd == "exit":
#         for _ in range(size()):
#             do()
#         print("Очередь пустая. Завершение работы")
#         break
#     else:
#         print("Введена неверная команда")

# представление графа в виде массива данных (словарь и список)
# metro = {
#     'адмиралтейская': ['садовая'],
#     'садовая': ['сенная площадь', 'спасская', 'адмиралтейская', 'звенигородская'],
#     'звенигородская': ['пушкинская', 'садовая'],
#     'пушкинская': ['звенигородская', 'владимирская'],
#     'сенная площадь': ['садовая', 'спасская'],
#     'спасская': ['садовая', 'сенная площадь', 'достоевская'],
#     'достоевская': ['владимирская', 'спасская']
# }

# создадим взвешенный граф
# metro = {
#     'адмиралтейская': {'садовая': 2},
#     'садовая': {'сенная площадь': 4,
#                 'спасская': 3,
#                 'адмиралтейская': 2,
#                 'звенигородская': 3},
#     'звенигородская': {'пушкинская': 3,
#                        'садовая': 3},
#     'пушкинская': {'звенигородская': 3,
#                    'владимирская': 2},
#     'сенная площадь': {'садовая': 4,
#                        'спасская': 3},
#     'спасская': {'садовая': 3,
#                  'сенная площадь': 3,
#                  'достоевская': 4},
#     'достоевская': {'владимирская': 3,
#                     'спасская': 4},
#     'владимирская': {'достоевская': 3,
#                      'пушкинская':2}
# }
#
# D = {k : 100 for k in metro.keys()}
# start_k = 'адмиралтейская'
# D[start_k] = 0
# U = {k : False for k in metro.keys()}
# P = {k : None for k in metro.keys()}

# for _ in range(len(D)):
#     min_k = min([k for k in U.keys() if not U[k]], key = lambda x: D[x])
#     for v in metro[min_k].keys():
#         D[v] = min(D[v], D[min_k] + metro[min_k][v])
#     U[min_k] = True
# for _ in range(len(D)):
#     min_k = min([k for k in U.keys() if not U[k]], key = lambda x: D[x])
#     for v in metro[min_k].keys():
#         if D[v] > D[min_k] + metro[min_k][v]:
#             D[v] = D[min_k] + metro[min_k][v]
#             P[v] = min_k
#     U[min_k] = True
# pointer = 'владимирская'
# while pointer is not None:
#     print(pointer)
#     pointer = P[pointer]

# class BinaryTree:
#     def __init__(self, value):
#         self.value = value
#         self.left_child = None
#         self.right_child = None
#
#     def insert_left(self, next_value):
#         if self.left_child is None:
#             self.left_child = BinaryTree(next_value)
#         else:
#             new_child = BinaryTree(next_value)
#             new_child.left_child = self.left_child
#             self.left_child = new_child
#         return self
#
#     def insert_right(self, next_value):
#         if self.right_child is None:
#             self.right_child = BinaryTree(next_value)
#         else:
#             new_child = BinaryTree(next_value)
#             new_child.right_child = self.right_child
#             self.right_child = new_child
#         return self
#
#     def post_order(self):
#         if self.left_child is not None:  # если левый потомок существует
#             self.left_child.post_order()  # рекурсивно вызываем функцию
#
#         if self.right_child is not None:  # если правый потомок существует
#             self.right_child.post_order()  # рекурсивно вызываем функцию
#
#         print(self.value)
#
#
# # создаём корень и его потомков /7|2|5\
# node_root = BinaryTree(2).insert_left(7).insert_right(5)
# # левое поддерево корня /2|7|6\
# node_7 = node_root.left_child.insert_left(2).insert_right(6)
# # правое поддерево предыдущего узла /5|6|11\
# node_6 = node_7.right_child.insert_left(5).insert_right(11)
# # правое поддерево корня /|5|9\
# node_5 = node_root.right_child.insert_right(9)
# # левое поддерево предыдущего узла корня /4|9|\
# node_9 = node_5.right_child.insert_left(4)
# node_root.post_order()


# class Node:  # класс элемента
#     def __init__(self, value=None, next_=None):  # инициализируем
#         self.value = value  # значением
#         self.next = next_  # и ссылкой на следующий элемент
#
#     def __str__(self):
#         return "Node value = " + str(self.value)
#
#
# class LinkedList:  # класс списка
#     def __init__(self):  # инициализируем пустым
#         self.first = None
#         self.last = None
#
#     def clear(self):  # очищаем список
#         self.__init__()
#
#     def __str__(self):  # функция печати
#         R = ''
#
#         pointer = self.first  # берем первый указатель
#         while pointer is not None:  # пока указатель не станет None
#             R += str(pointer.value)  # добавляем значение в строку
#             pointer = pointer.next  # идем дальше по указателю
#             if pointer is not None:  # если он существует добавляем пробел
#                 R += ' '
#         return R
#
#     def pushleft(self, value):
#         if self.first is None:
#             self.first = Node(value)
#             self.last = self.first
#         else:
#             new_node = Node(value, self.first)
#             self.first = new_node
#     def pushright(self, value):
#         if self.first is None:
#             self.first = Node(value)
#             self.last = self.first
#         else:
#             new_node = Node(value)
#             self.last.next = new_node
#             self.last = new_node
#
#     def popleft(self):
#         if self.first is None:  # если список пустой, возвращаем None
#             return None
#         elif self.first == self.last:  # если список содержит только один элемент
#             node = self.first  # сохраняем его
#             self.__init__()  # очищаем
#             return node  # и возвращаем сохраненный элемент
#         else:
#             node = self.first  # сохраняем первый элемент
#             self.first = self.first.next  # меняем указатель на первый элемент
#             return node  # возвращаем сохраненный
#
#     def popright(self):
#         if self.first is None:  # если список пустой, возвращаем None
#             return None
#         elif self.first == self.last:  # если список содержит только один элемент
#             node = self.first  # сохраняем его
#             self.__init__()  # очищаем
#             return node  # и возвращаем сохраненный элемент
#         else:
#             node = self.last  # сохраняем последний
#             pointer = self.first  # создаем указатель
#             while pointer.next is not node:  # пока не найдем предпоследний
#                 pointer = pointer.next
#             pointer.next = None  # обнуляем указатели, чтобы
#             self.last = pointer  # предпоследний стал последним
#             return node  # возвращаем сохраненный
#
#     def __iter__(self):  # объявляем класс как итератор
#         self.current = self.first  # в текущий элемент помещаем первый
#         return self  # возвращаем итератор
#
#     def __next__(self):  # метод перехода
#         if self.current is None:  # если текущий стал последним
#             raise StopIteration  # вызываем исключение
#         else:
#             node = self.current  # сохраняем текущий элемент
#             self.current = self.current.next  # совершаем переход
#             return node  # и возвращаем сохраненный
#
#     def __len__(self):
#         count = 0
#         pointer = self.first
#         while pointer is not None:
#             count += 1
#             pointer = pointer.next
#         return count
#
# LL = LinkedList()
#
# LL.pushright(1)
# LL.pushleft(2)
# LL.pushright(3)
# LL.popright()
# LL.pushleft(4)
# LL.pushright(5)
# LL.popleft()
#
# print(LL.__len__())

# def find(array, element):
#     for i, a in enumerate(array):
#         if a == element:
#             return i
#     return False
#
# array = list(map(int, input().split()))
# element = int(input())
#
# print(find(array, element))

# def count_(array, el):
#     count = 0
#     for i in array:
#         if i == el:
#             count +=1
#     return count
#
# array = list(map(int, input().split()))
# el = int(input())
#
# print(count_(array, el))


# def binary_search(array, element, left, right):
#     if left > right:  # если левая граница превысила правую,
#         return False  # значит элемент отсутствует
#
#     middle = (right + left) // 2  # находимо середину
#     if array[middle] == element:  # если элемент в середине,
#         return middle  # возвращаем этот индекс
#     elif element < array[middle]:  # если элемент меньше элемента в середине
#         # рекурсивно ищем в левой половине
#         return binary_search(array, element, left, middle - 1)
#     else:  # иначе в правой
#         return binary_search(array, element, middle + 1, right)
#
#
# element = int(input())
# array = [i for i in range(1, 100)]  # 1,2,3,4,...
#
# # запускаем алгоритм на левой и правой границе
# print(binary_search(array, element, 0, 99))

# наивная сортировка, как делать не надо
# import random  # модуль, с помощью которого перемешиваем массив
#
# # пусть имеем массив всего лишь из 9 элементов
# array = [x for x in range(1,101)]
#
# is_sort = False  # станет True, если отсортирован
# count = 0  # счетчик количества перестановок
#
# while not is_sort:  # пока не отсортирован
#     count += 1  # прибавляем 1 к счётчику
#
#     random.shuffle(array)  # перемешиваем массив
#
#     # проверяем, отсортирован ли
#     is_sort = True
#     for i in range(len(array) - 1):
#         if array[i] > array[i + 1]:
#             is_sort = False
#             break
#
# print(array)
# print(count)
# def fac(n):
#     if n == 0:
#         return 1
#     return fac(n - 1) * n
#
#
# print(fac(9))

# сортировка выбором
# array = [2, 3, 1, 4, 6, 5, 9, 8, 7]
# count = 0
# for i in range(len(array)):  # проходим по всему массиву
#     idx_min = i  # сохраняем индекс предположительно минимального элемента
#     for j in range(i, len(array)):
#         count += 1
#         if array[j] > array[idx_min]:
#             idx_min = j
#     if i != idx_min:  # если индекс не совпадает с минимальным, меняем
#         array[i], array[idx_min] = array[idx_min], array[i]
#
# print(array)

# сортировка пузырьком
# array = [2, 3, 1, 4, 6, 5, 9, 8, 7]
#
# for i in range(len(array)):
#     for j in range(len(array) - i - 1):
#         if array[j] > array[j + 1]:
#             array[j], array[j + 1] = array[j + 1], array[j]
#
# print(array)

array = [2, 3, 1, 4, 6, 5, 9, 8, 7]
# count =0
# for i in range(1, len(array)):
#     x = array[i] #6
#     idx = i #4
#     while idx > 0 and array[idx-1] > x:
#         count +=1
#         array[idx] = array[idx-1]
#         idx -= 1
#     array[idx] = x # [,2,3,4
#
# print(count)

#сортировка быстрая

def qsort(array, left, right):
    middle = (left + right) // 2

    p = array[middle]
    i, j = left, right
    while i <= j:
        while array[i] < p:
            i += 1
        while array[j] > p:
            j -= 1
        if i <= j:
            array[i], array[j] = array[j], array[i]
            i += 1
            j -= 1

    if j > left:
        qsort(array, left, j)
    if right > i:
        qsort(array, i, right)