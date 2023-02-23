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

# task #7
goods = list(map(int, input('Укажите число сувениров и безделушек к покупке через пробел: ').split()))
weights = (goods[0]*75 + goods[1]*112)/1000
print('Общий вес посылки составил %.3f кг' % weights)