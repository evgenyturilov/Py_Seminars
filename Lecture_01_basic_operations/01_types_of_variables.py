# типы данных и переменная
# int, float, boolean, str, list, None

a = 123
b = 1.23
print(type(a))
print(type(b))

value = None        # присваевает переменной тип None, после этого можно использовать неназванную пепеменную
                    # т.е. значение можно будет присвоить впоследствии
print(type(value))

value = 1234
print(type(value))

# работа со строковыми данными

s = 'hello world'
t = "hello 'world'" # можно t = 'hello "world"'
u = 'hello \nworld' # \n - оператор переноса на новую строку

print(s, t, u)

# логический тип данных 'bool'

f = True
print(type(f))