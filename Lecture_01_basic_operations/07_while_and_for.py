# примеры использования циклов при помощи операторов while, while-else и for

original = 23
inverted = 0
while original != 0:
    inverted = inverted * 10 + (original % 10)
    original //= 10
    print(inverted)
else:
    print('Пожалуй')
    print('хватит !')
print(inverted)

for i in 1,2,3,4,5,6:
    print(i ** 2)

list = range(10)        # range(1, 5, 2) - рейндж от, до, приращение
for i in list:
    print(i)

# вложенные циклы

line = ""
for i in range(5):
    line = ""
    for j in range(5):
        line += "*"
print(line)
