# 3. Реализовать функцию my_func(), которая принимает три позиционных аргумента и возвращает сумму наибольших двух аргументов.

def func(a, b, c):
    max1 = max(a, b, c)
    min1 = min(a, b, c)
    max2 = (a + b + c) - (max1 + min1)
    return max1 + max2


print(func(4, 2, 3))

# Железная логика.
