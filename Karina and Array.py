t = int(input())
while t:
    n = int(input())
    x = [int(x) for x in input().split()]
    x.sort()
    num1 = x[0] * x[1]
    num2 = x[-1] * x[-2]
    print(max(num1, num2))
    t -= 1
