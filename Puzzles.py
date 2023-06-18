n, m = [int(x) for x in input().split()]
x = [int(x) for x in input().split()]
y = []
x.sort()

i = 0
j = n - 1
while j < len(x):
    y.append(x[j] - x[i])
    i += 1
    j += 1
print(min(y))
