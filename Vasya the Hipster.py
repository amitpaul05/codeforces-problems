a, b = [int(x) for x in input().split()]
res1, res2 = 0, 0
if a < b:
    res1 = a
    res2 = (b - a) // 2
else:
    res1 = b
    res2 = (a - b) // 2

print(res1, res2)
