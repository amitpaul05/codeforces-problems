n, k = [int(x) for x in input().split()]
x = [int(x) for x in input().split()]
count = 0
for i in x:
    if i >= x[k-1] and i > 0:
        count += 1

print(count)