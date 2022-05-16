# Задача 19. Реализуйте алгоритм задания случайных чисел без использования генератора псевдослучайных чисел

import time

def random_number(min, max):
    now = str(time.time())
    print(now)
    rnd = int(now[::-1][:3:])/1000
    return min + rnd*(max-min)

print(round(random_number(1,10)))