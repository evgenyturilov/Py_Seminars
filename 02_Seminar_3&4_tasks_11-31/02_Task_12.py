# Задача №12. Для натурального n создать словарь индекс-значение, состоящий из элементов последовательности 3n + 1.
# Пример: для n = 6: {1: 4, 2: 7, 3: 10, 4: 13, 5: 16, 6: 19}

print('Введите целое число n:')
n = int(input())

dictionary = {}
for key in range(1, n + 1):
    dictionary[key] = 3*key + 1

print(dictionary)
