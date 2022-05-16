# Задача22.	Найти сумму чисел списка стоящих на нечетной позиции.

lst = [1,2,3,4]

sum = 0
for i in range(len(lst)):
    if i%2 == 0:
        sum += lst[i]

print(sum)