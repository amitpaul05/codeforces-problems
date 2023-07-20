n, k = [int(x) for x in input().split()]
mid = 0
if n % 2 == 0:
    mid = n // 2
else:
    mid = (n // 2) + 1
if k > mid:
    res = (k - mid) * 2
else:
    res = (k * 2) - 1
print(res)
