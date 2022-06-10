# 7. Реализовать генератор с помощью функции с ключевым словом yield, создающим очередное значение.
# При вызове функции должен создаваться объект-генератор.
# Функция вызывается следующим образом: for el in fact(n).
# Она отвечает за получение факториала числа. В цикле нужно выводить только первые n чисел, начиная с 1! и до n!.
# Подсказка: факториал числа n — произведение чисел от 1 до n. Например, факториал четырёх 4! = 1 * 2 * 3 * 4 = 24.

import math

def func (n):
    for i in range(1,n):
        yield f'Факториал !{i} = {math.factorial(i)} '

x = func(5)
for i in func(5):
    print(i)

# https://youtu.be/qbAYYjZ_Xro









# def my_pain(n):
#     for i in range(1,n):
#         yield i *
#
#
# g = my_pain(4)
# print (next(g))


# def my_pain(n):
#     res = []
#     for i in range(1,n):
#         res.append(i*i)
#         return res
#
#
# g = my_pain(4)
# print(g)
