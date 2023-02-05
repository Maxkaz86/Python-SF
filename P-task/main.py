per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}
just_pc = list(per_cent.values())
amount = int(input('money: '))
sum_in = amount * just_pc[0] / 100, amount * just_pc[1] / 100, amount * just_pc[2] / 100, amount * just_pc[3] / 100
deposit = list(map(int, sum_in))
print(deposit)
print('Максимальная сумма, которую вы можете заработать - %d у.е.' % (max(deposit)))
