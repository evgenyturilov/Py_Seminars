# Задача 36. Дан список чисел. Создать список, в который попадают числа, описывающие возрастающую последовательность.

nums = [1, 5, 3, 4, 6, 1, 7]

def sort_break(n):
    nums_2 =[n[0]]
    for i in range(len(n) - 1):
        if n[i] < n[i + 1]:
            nums_2.append(n[i + 1])
        else:
            excl_num = i
            break
    return excl_num

print(nums_2)
print(i)
del nums[1]
print(nums)
print(nums.pop(-1))
print(nums)