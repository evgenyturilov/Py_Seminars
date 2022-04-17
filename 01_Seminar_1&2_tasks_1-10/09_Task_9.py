# Задача 9. Указав номер четверти прямоугольной системы координат,
# показать допустимые значения координат для точек этой четверти.

def range_of_quarters(n):
    if n == 1:
        return 'от x = 0 до x = ∞; от y = 0 до y = ∞'
    elif n == 2:
        return 'от x = 0 до x = -∞; от y = 0 до y = ∞'
    elif n == 3:
        return 'от x = 0 до x = -∞; от y = 0 до y = -∞'
    elif n == 4:
        return 'от x = 0 до x = ∞; от y = 0 до y = -∞'

number_of_quarter = int(input('Введите номер четверти на плоскости(число от 1 до 4): '))
print(f'Допустимые значения координат для {number_of_quarter}-й четверти равны:')
print(range_of_quarters(number_of_quarter))