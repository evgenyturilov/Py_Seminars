# Задача 7. Проверить истинность утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.

flag = True
print('x', 'y', 'z', ' ', 'левая часть', ' ', 'правая часть')
for x in range(2):
    for y in range(2):
        for z in range(2):
            left_equation = not (x or y or z)
            right_equation = (not x and not y and not z)
            print(x, y, z, ' ',left_equation, '       ',right_equation)
            if left_equation != right_equation:
                 flag = False

if flag == True:
   print('\nУтверждение истино\n')
else:
    print('\nУтверждение ложно\n ')