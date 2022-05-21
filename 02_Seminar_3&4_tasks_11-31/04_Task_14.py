# Задача 14. Подсчитать сумму цифр в вещественном числе.

# Решение 1. С использованием встроенной функции count()

from itertools import count

num = (input('Введите вещественное число:'))

digit_value = len(num) - num.count('.') - num.count(',')
print(f'Количество цифр в вашем числе равняется {digit_value}')

# Решение 2. C применением lambda-функций и встроенного итератора map()

d_value = sum(map(lambda x: 1 if x != ('.' or ',') else 0, num))
print(f'Количество цифр в вашем числе равняется {d_value}')