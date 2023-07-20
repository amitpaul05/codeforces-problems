n = int(input())

x = [int(x) for x in input().split()]

y = [x.count(1), x.count(2), x.count(3)]

y.sort()

if y.count(0) > 0:
    print(0)
else:
    print(y[0])
    i, j, k = 0, 0, 0
    for l in range(y[0]):
        i = x.index(1, i) + 1
        j = x.index(2, j) + 1
        k = x.index(3, k) + 1
        print(i, j, k)


