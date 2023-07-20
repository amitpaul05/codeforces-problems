t = int(input())
res = 0
while t:
    n = int(input())
    if n % 2 == 0:
        res = (n // 2) - 1
    else:
        res = n // 2

    print(res)
    t -= 1
