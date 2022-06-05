# 3. Узнайте у пользователя число n. Найдите сумму чисел n + nn + nnn.
# Например, пользователь ввёл число 3. Считаем 3 + 33 + 333 = 369.

number = int(input('Введите число: '))
bred_1 = number + number
bred_2 = number + number + number

print(str(number) + str(bred_1) + str(bred_2))

