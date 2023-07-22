t = int(input())
x = []
while t:
    n = int(input())
    temp = []
    while n:
        a, b = [int(x) for x in input().split()]
        if a <= 10:
            temp.append(b)
        else:
            temp.append(-1)
        n -= 1
    print(temp.index(max(temp)) + 1)
    t -= 1
