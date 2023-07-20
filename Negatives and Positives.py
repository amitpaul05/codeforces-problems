t = int(input())
res = 0
while t:
    n = int(input())
    x = [int(x) for x in input().split()]
    x.sort()
    i = 0
    while x[i] < 0:
        x[i] = -(x[i])
        x[i+1] = -(x[i+1])
        i += 1
    res = sum(x)
    print(res)
    t -= 1