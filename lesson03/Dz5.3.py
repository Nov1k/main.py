# 5. Программа запрашивает у пользователя строку чисел, разделённых пробелом. При нажатии Enter должна выводиться сумма чисел.
# Пользователь может продолжить ввод чисел, разделённых пробелом и снова нажать Enter.
# Сумма вновь введённых чисел будет добавляться к уже подсчитанной сумме.
# Но если вместо числа вводится специальный символ, выполнение программы завершается.
# Если специальный символ введён после нескольких чисел, то вначале нужно добавить сумму этих чисел к полученной ранее сумме и после этого завершить программу.


def func_summa():
    result = 0
    while True:
        data = input('Введите числа через пробел : ').split()
        for i in data:

            # if i == 'stop':
            #     return
            # else:

            # нужен был конкретный специальный символ
            try:
                i = int(i)
                result += i
            except ValueError:
                return result , 'Вроде работает: '
        print (result)

print (func_summa())






# stroka = input('Введите числа через строку ').split()
# res = 0
# for i in stroka:
#     i = int(i)
#     res += i
# print(res)
#
# while True:
#     stroka = input('Введите числа через строку ').split()
#
#     for i in stroka:
#
#         i = int(i)
#         res += i
#     print(res)






# def stroka1(stroka1):
#
#         for i in stroka1:
#             i = int(i)
#             i += int(i)
#             res = i
#         return res
# print (stroka1(stroka))
# while True :
#     stroka = input('Введите числа через строку ').split()
#     print (stroka1(stroka))