# работа со списками


from ast import List


list_1 = [1, 3.5, 'rty', True]      # можно комбинировать переменные в списке(это не желательно)
col = [1, 2, 3, 4, 5, 6, 7, 8, 9]

print(list_1)

numbers = [1, 2, 3, 4, 5, 6, 7]
print(type(numbers))
ran = range(1,8)
print(type(ran))
numbers = list(ran)
print(type(numbers))
print(f'{len(numbers)} len')

for i in numbers:
    print(i ** 2)

print(numbers)

colors = ['red', 'green', 'blue', 'orange']
print(colors)
colors.remove('red')                        # можно удалить элемент из списка при помощи del colors[0]
print(colors)        
del colors[0]
print(colors)
colors.append('red')                        # append добавляет элемент в конец списка
print(colors)
