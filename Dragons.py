s, n = [int(x) for x in input().split()]
x = []
y = []
count = 0
for i in range(n):
    a, b = [int(x) for x in input().split()]
    x.append(a)
    y.append(b)
maximum = x.index(max(x))
if x.count(max(x)) > 1:
    maxi = [i for i, a in enumerate(x) if a == max(x)]
    minimum = y[maxi[0]]
    for i in range(1, len(maxi)):
        if minimum > y[maxi[i]]:
            minimum = y[maxi[i]]
            maximum = maxi[i]

s = (sum(y) + s) - y[maximum]
for i in x:
    if s < i:
        print("NO")
        exit()
print("YES")