import math
t = int(input())
sum = 0
while t:
    n = int(input())
    x = [int(x) for x in input().split()]
    for i in range(1, n+1):
        sum += (math.pow((-1), i)*x[i])
    t -= 1