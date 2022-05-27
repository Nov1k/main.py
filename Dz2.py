# 2.Пользователь вводит время в секундах. Переведите время в часы, минуты, секунды и выведите в формате чч:мм:сс.
# Используйте форматирование строк.

second = int(input("Введите любое колличество секунд: "))
second1 = second % 60

minute = second // 60
minute1 = minute % 60

hour = minute // 60


print('Секунд: ', second1)
print ('Минут: ', minute1)
print ('Часов: ', hour)

print (f"Время: {hour}:{minute1}:{second1}")


