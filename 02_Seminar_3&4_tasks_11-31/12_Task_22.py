# Задача22.	Найти сумму чисел списка стоящих на нечетной позиции.

lst = [1,2,3,4]

# Решение 1 (алгоритмическое)

summ = 0
for i in range(len(lst)):
    if i%2 != 0:
     summ += lst[i]
print(summ)

# Решение 2 (list comprehention)

print(sum([lst[i] for i in range(len(lst)) if i%2]))

# Решение 3 (lambda + filter())

print(sum(list(filter(lambda i: not i%2, lst))))