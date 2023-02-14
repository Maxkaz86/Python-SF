tickets = int(input('Введите количество билетов: '))
if tickets > 3:
    print('Вам доступна скидка 10% при регистрации 4 и более участников')
ages = list(map(int, input('Укажите возраст посетителей через пробел, согласно количеству билетов: ').split()))
if len(ages) != tickets:
    print('Вы не указали возраст всех участников. Укажите возраст всех участников!')
    ages = list(map(int, input('Укажите возраст посетителей через пробел: ').split()))
sum_ticket = []
for i in ages:
    if i < 18:
        sum_ticket.append(0)
    elif 18 <= i < 25:
        sum_ticket.append(990)
    else:
        sum_ticket.append(1390)
if tickets > 3:
    sum_disc = round(sum(sum_ticket) - (sum(sum_ticket) * 0.1))
    print('Сумма к оплате с учетом скидки: ', sum_disc, 'руб.')
else:
    print('Сумма к оплате: ', sum(sum_ticket), 'руб.')