# Задача 17. Задать список из N элементов, заполненных числами из [-N, N].
# Найти произведение элементов на указанных позициях. Позиции хранятся в файле file.txt в одной строке одно число

n = 10
numbers = [i for i in range(-n, n + 1)]

with open(r'D:\GB_Developer\1.6 Знакомство с Python\Python\Py_Seminars\02_Seminar_3&4_tasks_11-31\07_Task_17_file.txt', 'r') as file:
    pos = file.read().splitlines()

pos = list(map(int, pos))

mult = 1
for i in pos:
    mult *= numbers[i]

print(numbers)
print(pos)
print(mult)
