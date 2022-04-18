# Задача 4. Показать первую цифру дробной части числа.

number = input('Введите вещественное число: ')
print(number)
# print(type(number))
# print(len(number))

def find_digit(n):
    for i in range(len(number) - 1):
        if number[i] == '.' or ',':
            result_digit = number[i + 1]
    return result_digit
        
print('Первая цифра дробной части числа:')
print(find_digit(number))
