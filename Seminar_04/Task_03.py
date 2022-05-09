# Считайте два числа из файла (одно число в одной строке). Напишите программу нахождения наименьшего общего кратного этих двух чисел.

from distutils import text_file


def read_file(text_file):                   # Функция построчного считывания чисел из файла и преобразования их в список целых чисел, используем метод splitlines
    with open(text_file, 'r') as file:
        nums = file.read().splitlines()
        
    for i in range(len(nums)):
        nums[i] = int(nums[i])
    return nums

def read_file_2(text_file):                 # Функция построчного считывания данных из файла и преобразования их в список целых чисел, используем построчное считывание из файла
    file = open(text_file, 'r')
    nums = list()
    for i in file:
        nums.append(int(i))
    return(nums)



text_file = 'd:/GB_Developer/1.6 Знакомство с Python/Python/Py_Seminars/Seminar_04/info.txt'


# my_file = open('d:/GB_Developer/1.6 Знакомство с Python/Python/Py_Seminars/Seminar_04/info.txt', 'r')
# numbers = my_file.readlines()
# my_file.close()

print(read_file_2(text_file))


# with open('info.txt', 'r') as file:
#    number_one = int(file.readlines())

# print(number_one)