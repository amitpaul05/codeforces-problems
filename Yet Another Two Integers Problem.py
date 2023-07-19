t = int(input())
while t:
    a, b = [int(x) for x in input().split()]
    res = 0
    max = a
    min = b
    if a < b:
        max = b
        min = a
    sub = max - min
    if sub % 10 == 0:
        res = sub // 10
    else:
        res = (sub // 10) + 1
    print(res)
    t -= 1