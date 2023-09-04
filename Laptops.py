# n = int(input())
# a = []
# b = []
# for i in range(n):
#     x = [int(x) for x in input().split()]
#     a.append(x[0])
#     b.append(x[1])
# length = len(a)
# main_a = a[:]
# main_b = b[:]
# a.sort()
# b.sort()
#
# happy = False
# for i in range(n):
#
#     if main_a.index(a[i]) != main_b.index(b[i]):
#         happy = True
#         break
# if happy:
#     print('Happy Alex')
# else:
#     print('Poor Alex')

n = int(input())

a = [0 for i in range(n + 1)]
for i in range(n):
    x = [int(x) for x in input().split()]
    a[x[0]] = x[1]
count = 0
for i in range(1, n):
    if a[i] > a[i + 1]:
        count = 1
        break
if count == 1:
    print('Happy Alex')
else:
    print('Poor Alex')
