# Задача 7. Проверить истинность утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.

array_of_X = [True, False]
array_of_Y = [True, False]
array_of_Z = [True, False]

def find_trueness(x, y, z):
    flag = True
    for i in range(0, 2):
        for j in range(0, 2):
            for k in range(0, 2):
                f1 = not (x[i] or y[j] or z[k])
                f2 = (not x[i] and not y[i] and not z[k])
                if f1 != f2:
                    flag = False
    return flag

if find_trueness(array_of_X, array_of_Y, array_of_Z) == True:
    print('Условие выполняется для любых значений x, y, z')
else:
    print('Условие не выполняется')