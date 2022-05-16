# Задача 35. В файле находится N натуральных чисел, записанных через пробел. Среди чисел не хватает одного, чтобы выполнялось условие A[i] - 1 = A[i-1]. Найти его.

with open(r'D:\GB_Developer\1.6 Знакомство с Python\Python\Py_Seminars\03_Seminar_5&6_tasks_32-44\04_Task_35_file.txt', 'r') as file:
    list_of_nums = file.read()

def find_missing_num(lst):
    for i in range(1, len(lst)):
        if lst[i] - 1 == lst[i - 1]:
            continue
        else:
            lst = lst[i] - 1
            break
    return lst

list_of_nums = list(map(int, list_of_nums.split()))
missing_num = (find_missing_num(list_of_nums))
print(f'Пропущенное число в заданном ряду натуральных чисел равняется: {missing_num}')



