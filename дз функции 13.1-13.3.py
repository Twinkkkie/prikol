# 13.1
def summa(list_1):
    sum_list = []
    for i in list_1:
        summ = 0
        while i:
            digit = i % 10
            summ = summ + digit
            i = i // 10

        sum_list.append(summ)
        sorted(sum_list)
    return sum_list


ls = [int(i) for i in input().split()]
print(ls, summa(ls))


# 13.2
def f(x):
    if x <= -2:
        return 1 - (x + 2) * (x + 2)
    elif -2 < x <= 2:
        return -x / 2
    else:
        return (x - 2) * (x - 2) + 1


num = float(input())
print(f(num))


# # 13.3 ???
# def new(ls):
#     new_ls = []
#     for i in ls:
#         while i:
#             if i % 2 == 0:
#                 new_i = i // 2
#                 new_ls.append(new_i)
#             else:
#                 del(i)
#     return new_ls
#
#
# list_1 = [int(i) for i in input().split()]
# print(new(list_1))