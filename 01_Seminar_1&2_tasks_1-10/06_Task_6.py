# Задача 6. Дано число, обозначающее день недели.
# Вывести его название и указать является ли он выходным.

days_of_week = ['Понедельник', 'Вторник', 'Среда', 'Четверг', 'Пятница', 'Суббота', 'Воскресенье']
# days_of_week_2 = ['Понедельник', 'Вторник', 'Среду', 'Четверг', 'Пятницу', 'Субботу', 'Воскресенье']

def is_weekend(n):
    if n - 1 == 5 or n - 1 == 6:
        return True

your_day = int(input('введите номер дня недели: '))
if is_weekend(your_day) == True:
    print(f'{days_of_week[your_day - 1]} - выходной.')
else:
    print(f'{days_of_week[your_day - 1]} - рабочий день.')