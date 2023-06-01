m, n, a = [int(x) for x in input().split()]

if m > a and n > a:
    x = 0
    if m % a == 0:
        x = m // a
    else:
        x = (m // a) + 1
    y = 0
    if n % a == 0:
        y = n // a
    else:
        y = (n // a) + 1
    res = x * y
    print(res)
elif m <= a and n <= a:
    print(1)
elif m > a >= n:
    if m % a == 0:
        x = m // a
    else:
        x = (m // a) + 1
    print(x)
elif n > a >= m:
    if n % a == 0:
        y = n // a
    else:
        y = (n // a) + 1
    print(y)
