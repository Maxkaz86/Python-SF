per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}
just_val = list(per_cent.values())
pc_con = []
amount = int(input('money: '))
deposit = []
for pc in just_val:
    pc_con.append(round(pc / 100, 3))
for i in pc_con:
    deposit.append(int(amount * i))
# sum_in = amount * just_pc[0] / 100, amount * just_pc[1] / 100, amount * just_pc[2] / 100, amount * just_pc[3] / 100
# deposit = list(map(int, sum_in))
# print(deposit)
print('Максимальная сумма, которую вы можете заработать - %d у.е.' % (max(deposit)))
