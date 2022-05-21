# Задача 18. Реализовать алгоритм перемешивания списка. 

import random

phrase = "Существует два рычага управления людьми: первый — это личная выгода, а второй — это деньги."
lst = phrase.split()


def shuffle(lst):
    for i in range(10):
        tmp = lst[i]
        m = random.randint(1, len(lst))
        lst[i] = lst[m]
        lst[m] = tmp
    return(' '.join(lst))

print(shuffle(lst))