# 2. Выполнить функцию, которая принимает несколько параметров, описывающих данные пользователя:
# имя, фамилия, год рождения, город проживания, email, телефон.
# Функция должна принимать параметры как именованные аргументы.
# Осуществить вывод данных о пользователе одной строкой.

def options(name, surname, years, city, email, phone):
    result = (f'\n{name} {surname} , {years} года рождения.\n'
              f'Проживает в городе: {city}\n'
              f'Email: {email}\n'
              f'Номер телефона: {phone}')
    return result


name = input('Введите ваше имя: ')
surname = input('Введите вашу фамилию: ')
years = int(input('Введие ваш год рождения: '))
city = input('Введите ваш город проживания: ')
email = input('Введите ваш "email" : ')
phone = int(input('Введите ваш номер телефона: '))

print(options(name, surname, years, city, email, phone))
