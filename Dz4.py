# 4. Пользователь вводит целое положительное число. Найдите самую большую цифру в числе.
#  Для решения используйте цикл while и арифметические операции.


num = int (input("Введите число: "))

maxi = 0
while num > 0:
    last = num % 10
    if last > maxi:
        maxi = last
    num = num // 10



print (maxi)





