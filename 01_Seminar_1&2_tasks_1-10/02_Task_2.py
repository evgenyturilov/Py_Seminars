# Задача 2. Найти максимальное из пяти чисел

def find_max(array):
    max = array[0]
    for i in range(0, len(array) - 1):
        if array[i] > max:
            max = array[i]
            return max

numbers = [3, 7, 4, 5, 1]
print(f'Наибольшее число из {numbers} - {find_max(numbers)}')
