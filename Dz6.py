# 6. Если фирма отработала с прибылью,
# вычислите рентабельность выручки. Это отношение прибыли к выручке.
# Далее запросите численность сотрудников фирмы и определите прибыль фирмы в расчёте на одного сотрудника.

all = int(input('Введите общую выручку: '))
plus = int(input("Введите прибыль: "))
rentabel = (plus / all) * 100

print (f'Рентабельность выручки равна: {rentabel}%')

members = int (input('Введите число сотрудников: '))
zp_members = 30000

plus_company = plus - zp_members * members
print(f'Чистая прибыль фирмы: {plus_company}')
