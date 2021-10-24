# 9.7
a = set(input())
b = set(input())
set_1 = a & b
print(*set_1)

# 9.8
a = set(input())
b = set(input())
print(*(a - b))

# 9.9
# Программа принимает 2 списка чисел. Найти сумму максимального и минимального элементов двух списков
nums_1 = [int(i) for i in input().split()]
nums_2 = [int(i) for i in input().split()]
set_0 = set(nums_1 + nums_2)
print(set_0)
sum_0 = min(set_0) + max(set_0)
print(sum_0)