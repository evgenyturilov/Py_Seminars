# Задача 10. Найти расстояние между двумя точками пространства

def find_distance(x1, x2, y1, y2):
    if x1 >= x2:
        x = x1 - x2
    else:
        x = x2 - x1

    if y1 >= y2:
        y = y1 - y2
    else:
        y = y2 - y1

    distance = (x ** 2 + y ** 2) ** 0.5
    return distance

print('Введите координаты первой точки: ')
x1 = int(input())
y1 = int(input())
print('Введите координаты второй точки: ')
x2 = int(input())
y2 = int(input())

print(f'Расстояние между точками - {round(find_distance(x1, x2, y1, y2), 7)}')

