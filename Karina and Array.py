t = int(input())
while t:
    n = int(input())
    x = [int(x) for x in input().split()]
    x.sort()
    n1 = x[0] * x[1]
    n2 = x[-1] * x[-2]
    print(max(n1, n2))
    t -= 1
