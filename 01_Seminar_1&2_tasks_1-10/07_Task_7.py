# Задача 7. Проверить истинность утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.

x = [True, False]
y = [True, False]
z = [True, False]

print('x', '  ', 'y', '  ', 'z', '     ', 'assumption_1', ' ', 'assumption_2')
flag = True
for i in range(0, 2):
        for j in range(0, 2):
            for k in range(0, 2):
                assumption_1 = not (x[i] or y[j] or z[k])
                assumption_2 = not x[i] and not y[i] and not z[k]
                print(x[i], y[j], z[k],'  ', assumption_1, '        ', assumption_2)
                if assumption_1 != assumption_2:
                    flag = False

if flag == True:
   print('\nУтверждение истино\n')
else:
    print('\nУтверждение ложно\n ')