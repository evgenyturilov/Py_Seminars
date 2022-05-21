# Написать программу, получающую набор произведений чисел от 1 до N.
# Пример: пусть N = 4, тогда [ 1, 2, 6, 24 ]

n = 4
nums = [i for i in range(1, n + 1)]
print(nums)

nums_2 = []
for i in range(len(nums) + 1):
    if i == 0:
        nums_2.append(1)
    else:
        nums_2.append(nums[i-1]*i)

print(nums_2)
    


#print(list(map(lambda x: (x - 1)*x, nums)))
