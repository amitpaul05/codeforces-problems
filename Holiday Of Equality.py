n = int(input())
res = 0
x = [int(x) for x in input().split()]
x.sort(reverse=True)
for i in range(1, n):
    if x[i] < x[0]:
        tk = x[0] - x[i]
        res += tk
print(res)
