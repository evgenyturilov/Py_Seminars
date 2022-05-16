# Задача 28. Создайте функцию для нахождения корней квадратного уравнения Ax2 + Bx + C = 0

print('Квадратное уравнение типа Ax2 + Bx + C = 0')
print('Введите A:')
a = int(input())
print('Введите B:')
b = int(input())
print('Введите C:')
c = int(input())

def square_equal(a, b, c):
    d = b**2 - 4*a*c
    if d > 0:
        print(f'Корни квадратного уравнения равны х1 = {(-b + d**0.5)/(2*a)}, х2 = {(-b - d**0.5)/(2*a)}')
    elif d == 0:
        print(f'Корень квадратного уравнения равен {-(b/2*a)}')
    else:
        print('У данного квадратного уравнения корней нет')

square_equal(a, b, c)