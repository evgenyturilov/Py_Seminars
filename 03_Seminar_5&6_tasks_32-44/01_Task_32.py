# Задача 32. Дана последовательность чисел. Получить список неповторяющихся элементов исходной последовательности.

# Для начала создадим последовательность случайных чисел (от 0 до 10 для увеличения вероятности повторения элементов списка)

import random
list_of_numbers = list()

for i in range(0,15): list_of_numbers.append(random.randint(0,10)) 
print(list_of_numbers)

# Решение 1. Алгоритмическое. Функция создает список из неповторяющихся элементов исходного списка без упорядочивания

def sort(nums):                                     
    sorted_nums = []
    for num in nums:
        if num in sorted_nums:
            continue
        else:
            sorted_nums.append(num)
    return sorted_nums

print(sort(list_of_numbers))

# Решение 2

print(list(set(list_of_numbers)))