# 2 . Для списка реализовать обмен значений соседних элементов. Значениями обмениваются элементы с индексами 0 и 1,
# 2 и 3 и т. д. При нечётном количестве элементов последний сохранить на своём месте. Для заполнения списка элементов
# нужно использовать функцию input().

ai = input('Введите данные через пробел: ').split()
first_number = 0
change_number = 1
while (len(ai) - 1) > change_number or len(ai) == 1:
    ai[first_number] , ai[change_number] = ai[change_number] , ai[first_number]
    first_number += 2
    change_number += 2
print(ai)

#ai[0] , ai[1] = ai[1] , ai[0]

