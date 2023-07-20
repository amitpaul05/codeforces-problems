t = int(input())

while t:
    a, b = [int(x) for x in input().split()]
    count = 0
    if a % b != 0:
        m = a % b
        count = b - m
    print(count)
    t -= 1
