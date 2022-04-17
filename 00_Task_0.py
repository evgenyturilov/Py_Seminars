# На вход подается число, необходимо вывести квадрат этого числа

def square(n):
    return n ** 2

number = int(input('Введите число: '))
print(f'Квадрат числа {number} равняется {square(number)}')
