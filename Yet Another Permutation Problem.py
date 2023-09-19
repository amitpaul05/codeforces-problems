t = int(input())

while t:
    n = int(input())
    res = [1]
    if n >= 2:
        i = 2
        while i <= n:
            j = i
            while j <= n:
                res.append(j)
                j = j * 2
            if i == 2:
                i += 1
            else:
                i += 2
    for x in res:
        print(x, end=' ')
    print()
    t -= 1
