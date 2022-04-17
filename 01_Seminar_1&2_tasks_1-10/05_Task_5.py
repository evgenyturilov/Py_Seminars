# Задача 5. Дано число. Проверить кратно ли оно 5 и 10 или 15, но не 30

def is_correspond(n):
    if  n % 30 == 0:
        return False
    elif (n % 5 == 0 and n % 10 == 0) or (n % 15 == 0):
        return True
    else:
        return False

number = int(input('Введите число: '))
if is_correspond(number) == True:
    print('Условия задачи выполняются')
else:
    print('Число не удовлетворяет условиям задачи')