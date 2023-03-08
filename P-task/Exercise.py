# task #1
# print('Меня зовут Максим.')
# print('Мой адрес: г. Воронеж, ул. Ленина, д. 1')

# task #2
# name = input('Введите имя: ')
# print(f'Добро пожаловать, {name}!')

# task #3
# params = list(map(float, input('Укажите длину и ширину комнаты в метрах через пробел: ').split()))
# square = params[0] * params[1]
# print(params)
# print(f'Площадь комнаты равна {square} метров')

# task #4
# params = list(map(int, input('Укажите длину и ширину участка в фунтах через пробел: ').split()))
# sq = (params[0] * params[1])/43560
# print('Площадь участка составляет %2.3f акра.' % sq)

# task #5
# bottle_small = int(input('Укажите кол-во бутылок объемом до 1 литра включительно: '))
# bottle_big = int(input('Укажите кол-во бутылок объемом свыше 1 литра: '))
# price_small = 0.1
# price_big = 0.25
# _sum = (bottle_small * price_small) + (bottle_big * price_big)
# print('Сумма к уплате: $%.2f' % _sum)

# task #6
# order = int(input('Укажите сумму заказа: '))
# tax = 0.2
# sum_tax = order*tax
# tips = 0.18
# sum_tips = order*tips
# summary = order+sum_tax+sum_tips
# print('Сумма налога - %.2f, чаевые - %.2f. Итого к уплате: %.2f' % (sum_tax, sum_tips, summary))

# # task #7
# numbers = int(input('Введите число: '))
# sum_numbers = int((numbers*(numbers+1))/2)
# print(f'Сумма чисел числа {numbers} равна', sum_numbers)

# task #8
# goods = list(map(int, input('Укажите число сувениров и безделушек к покупке через пробел: ').split()))
# weights = (goods[0]*75 + goods[1]*112)/1000
# print('Общий вес посылки составил %.3f кг' % weights)

# # task #9
# amount = int(input('Укажите сумму депозита: '))
# per_cent = 0.04
# deposit_one = amount + (amount*per_cent)
# deposit_two = deposit_one + (deposit_one*per_cent)
# deposit_three = deposit_two + (deposit_two*per_cent)
# print('Сумма депозита за первый год: %.2f у.е.' % deposit_one)
# print('Сумма депозита за второй год: %.2f у.е.' % deposit_two)
# print('Сумма депозита за третий год: %.2f у.е.' % deposit_three)

# task #10
# import math
# a = int(input('введите число а: '))
# b = int(input('введите число b: '))
# print(a + b)
# print(a - b)
# print(a * b)
# print(a // b)
# print(a % b)
# print(math.log10(a))
# print(a ** b)

# task #11
# petrol = int(input('Сколько потребляет топлива ваш автомобиль в MPG: '))
# ml_to_km = petrol * 1.61
# gal_usa = 3.785411784
# litre = int(gal_usa/ml_to_km * 100)
# print('Потребление топлива л/100км:', litre)

# task #12
# import math
# point_one = list(map(int, input('Укажите широту и долготу первой точки в градусах через пробел: ').split()))
# point_two = list(map(int, input('Укажите широту и долготу второй точки в градусах через пробел: ').split()))
# t1 = math.radians(point_one[0])
# g1 = math.radians(point_one[1])
# t2 = math.radians(point_two[0])
# g2 = math.radians(point_two[1])
# distance = int(6371.01 * math.acos(math.sin(t1)*math.sin(t2) + math.cos(t1)*math.cos(t2)*math.cos(g1-g2)))
# print('Кратчайшее расстояние между 2 точками в км: ', distance)

# task #13
# changes = float(input('Введите сумму сдачи в центах: '))
# toonie = changes // 200
# _toonie = changes % 200
# loonie = _toonie // 100
# _loonie = _toonie % 100
# quarter = _loonie // 25
# _quarter = _loonie % 25
# ten = _quarter // 10
# _ten = _quarter % 10
# five = _ten // 5
# _five = _ten % 5
# two = _five // 2
# _two = _five % 2
# coin = _two
# print('Ваша сдача:', '\n', f'2 дол. - {toonie} шт.', '\n', f'1 дол. - {loonie} шт.',
#       '\n', f'25 цент. - {quarter} шт.''\n', f'10 цент. - {ten} шт.''\n', f'5 цент. - {five} шт.''\n',
#       f'2 цент. - {two} шт.''\n', f'1 цент - {coin} шт.')

# task #14
# tall = list(map(int, (input('Укажите ваш рост в формате фут/пробел/дюйм: ').split())))
# print('Ваш рост в см -', int(tall[0]*12 + tall[1]*2.54))

# task #15
# distance = int(input('Введите расстояние в футах: '))
# inches = distance * 12
# yards = distance * 0.33
# miles = distance * 0.00019
# print(f'Расстояние {distance} футов эквивалентно {inches} дюймам или {yards} ярдам, или {miles} милям')

# task #16
import math
r = int(input('Укажите радиус: '))
area = math.pi * r ** 2
v = 4/3 * math.pi * (r ** 3)
print(f'Площадь круга - {area}, объем шара - {v}')