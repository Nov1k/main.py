# 4. Пользователь вводит строку из нескольких слов, разделённых пробелами.
# Вывести каждое слово с новой строки. Строки нужно пронумеровать.
# Если слово длинное, выводить только первые 10 букв в слове.

ai = input('Введите несколько слов через пробел: ').split()
for i, elprimo in enumerate(ai):
    if len(elprimo) > 9:
        print(i + 1, elprimo[0:10])
    else:
        print(i + 1, elprimo)

# 2 Вариант
# for i, elprimo in enumerate(ai):
#     print((i + 1, elprimo[0:10]) if len(elprimo) > 9 else (i + 1, elprimo))
#
#     Не работает без скобок...
#     print(i + 1, elprimo[0:10] if len(elprimo) > 9 else i + 1, elprimo)
