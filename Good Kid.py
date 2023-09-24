t = int(input())

while t:
    n = int(input())
    x = [int(x) for x in input().split()]
    i = x.index(min(x))
    x[i] = x[i] + 1
    mul = 1
    for i in x:
        mul = mul * i
    print(mul)
    t -= 1