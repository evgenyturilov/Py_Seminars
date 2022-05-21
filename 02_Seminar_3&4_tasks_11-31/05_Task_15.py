# Написать программу, получающую набор произведений чисел от 1 до N.
# Пример: пусть N = 4, тогда [ 1, 2, 6, 24 ]

n = 4
nums = [i for i in range(1, n + 1)]
nums.insert(0, 0)
print(nums)

nums_2 = []
for i in range(1 ,len(nums)):
    if i == 1:
        nums_2.append(1)
    else:
        nums_2.append(nums[i-1]*i)
        nums[i] = nums[i-1]*i

print(nums_2)
