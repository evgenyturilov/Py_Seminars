# Задача 21. Напишите программу, которая определяет позицию второго вхождения строки в списке, либо сообщит, что ее нет.
# Пример:
#           ["qwe", "asd", "zxc", "qwe", "ewq"] - ищем "qwe", ответ:    3
#           ["123", "234", 123, "567", "789"]   - ищем "123", ответ:    -1
#           []                                  - ищем "123", ответ:    -1

# Решение №1 (моё)

my_list = ["qwe", "wer", "ert", "rty", "qwe", "yui", "qwe"]
string_to_find = "qwe"
flag = -1
count = 0 

for i in range(len(my_list)):
    if my_list[i] == string_to_find:
        count += 1
        if count == 2:
            flag = i
            break

print(flag)

# Решение №2

my_list_2 = ["qwe", "wer", "ert", "rty", "qwe", "yui", "qwe", "rty"]
list_2 = [i for i,x in enumerate(my_list_2) if x == "wer"]
if len(list_2) > 1: print(list_2[1])
else: print('-1')