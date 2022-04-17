# Задача 8. Сообщить в какой четверти координатной плоскости
# или на какой оси находится точка с координатами Х и У

def where_is_point(x, y):
    if x == 0:
        return 'на оси Y'
    elif y == 0:
        return 'на оси X'
    elif x > 0 and y > 0:
        return 'в I-й четверти координатной плоскости'
    elif x < 0 and y > 0:
        return 'во II-й четверти координатной плоскости'
    elif x > 0 and y < 0:
        return 'в VI-й четверти координатной плоскости'
    elif x < 0 and y < 0:
        return 'в III-й четверти координатной плоскости'

print('Введите координаты точки: ')
coord_x = int(input())
coord_y = int(input())
print(f'Ваша точка расположена {where_is_point(coord_x, coord_y)}')