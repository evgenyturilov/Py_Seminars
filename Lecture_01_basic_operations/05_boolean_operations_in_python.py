# >, >=, <, <=, ==, !=
# not, and, or – не путать с &, |, ^
# Кое-что ещё: is, is not, in, not in

a = 1 > 4 and 5 > 2
print(a)

b = 4 > 1 or 4 < 1
print(b)

a = [1,2]
b = [1,2]
print( a == b)

c = 1 > 5 < 6 < 8
print(c)

f = [1,2,2,3,4,5,6]
print(f)
print(2 in f)
print(not 5 in f)

is_odd = f[0] % 2 == 0      # или можно записать is_odd = not f[0] % 2 т.к. интерпретатор воспринимает 1 как True, 0 как False
print(is_odd)