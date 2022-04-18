# Задача 4. Показать первую цифру дробной части числа.

number = input('Введите вещественное число: ')

def find_digit(number):
    if '.' in number or ',' in number:
        for i in range(len(number) - 1):
            if number[i] == '.' or number[i] == ',':
                result_digit = number[i + 1]
                return (f'Первая цифра дробной части числа: {result_digit}')
    else:
        return ('Вы ввели целое число')

print(find_digit(number))
