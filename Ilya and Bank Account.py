x = int(input())

if x > 0:
    print(x)
else:
    x = abs(x)
    a = -(x // 10)
    b = -(x // 100)*10 - (x % 10)
    print(max(a, b))



