# 3. Пользователь вводит месяц в виде целого числа от 1 до 12.
# Сообщить, к какому времени года относится месяц (зима, весна, лето, осень).
# Напишите решения через list и dict.

#                    list

mouth = ['', 'Winter', 'Winter',
         'Spring', 'Spring', 'Spring',
         'Summer', 'Summer', 'Summer',
         'Autumn', 'Autumn', 'Autumn', 'Winter' ]

num = int(input('Введите месяц в виде целого числа от 1 до 12: '))
while num > 12 or num < 1:
    num = int(input('Вы ввели некорректное число, потворите попытку: '))
print(mouth[num])


#                    2 решение dict
# Mouth = {
#     'Winter': [12,1,2],
#     'Spring': [3,4,5],
#     'Summer': [6,7,8],
#     'Autumn': [9,10,11]
# }
# num = int(input('Введите месяц в виде целого числа от 1 до 12: '))
# while num > 12 or num < 1:
#     num = int(input('Вы ввели некорректное число, потворите попытку: '))
#
# for i in Mouth:
#     if num in Mouth[i]:
#         print(i)
#         break

