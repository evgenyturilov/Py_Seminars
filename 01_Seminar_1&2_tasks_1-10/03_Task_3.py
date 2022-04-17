# Задача 3. Вывести на экран числа от -N до N

def number_range(n):
    numbers = []
    for i in range(-n, n + 1):
        numbers.append(i)

    return numbers

number = int(input('Введите число:'))
print(f'Числа от {-number} до {number}:')
print(number_range(number))
