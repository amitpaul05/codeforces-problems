
# if n == 1:
#     num = t
#     if t > 9:
#         num = -1
# else:
#     num = 2 * (10 ** (n - 1))
#     num = num - (num % t)
# print(num)
n, t = [int(x) for x in input().split()]
num = 10**n - 1
if num < t:
    num = -1
else:
    num = num - (num % t)
print(num)