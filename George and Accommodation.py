t = int(input())
count = 0
while t:
    x = [int(x) for x in input().split()]
    n = x[1] - x[0]
    if n >= 2:
        count += 1
    t -= 1
print(count)
