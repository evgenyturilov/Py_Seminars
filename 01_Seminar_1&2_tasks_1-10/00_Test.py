#my_list = []
#for i in range(11):
#    my_list.append(i)
#
#for item in my_list:
#    if not item%2 == 0:
#         print(item**2)

# Задайте список. Напишите программу, которая определит присутствует ли некое число в заданном списке

# Решение №1

my_list = [1, 5, 76, 78, 54, 32]
num_to_find = int(input('Введите искомое число: '))

if num_to_find in my_list:
    print(f'{num_to_find} есть в списке')


# Решение №2 (Алгоритмическое)

my_list_2 = [2, 5, 8, 9, 45, 23, 17]
num = 17
flag = -1

for i in range(len(my_list_2)):
    if my_list_2[i] == num:
        flag = i
        break

if flag != -1:
    print(f'Число {num} есть в списке на позиции {flag}')
