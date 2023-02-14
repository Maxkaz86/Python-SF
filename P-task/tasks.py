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

text = input()  # получаем строку

first = text[0]  # сохраняем первый символ
count = 0  # заводим счетчик
result = ''  # и результирующую строку

for c in text:
    if c == first:  # если символ совпадает с сохраненным,
        count += 1  # то увеличиваем счетчик
    else:
        result += first + str(count)  # иначе - записываем в результат
        first = c  # и обновляем сохраненный символ с его счетчиком
        count = 1

result += first + str(count)  # и добавляем в результат последний символ
print(result)

