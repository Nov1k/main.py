# 5. Реализовать формирование списка, используя функцию range() и возможности генератора.
# В список должны войти чётные числа от 100 до 1000 (включая границы). Нужно получить результат вычисления произведения всех элементов списка.
# Подсказка: использовать функцию reduce().
import functools


spisok = [i for i in range(100, 1001) if i % 2 == 0]
new = functools.reduce(lambda x, y: x * y, spisok)

print(new)




# test_spisok = [1, 2, 3]
# new_2 = functools.reduce(lambda x, y: x * y, test_spisok)