x = [int(x) for x in input().split("+")]

x.sort()
l = len(x)
for i in range(l):
    if l-1 == i:
        print(x[i])
    else:
        print(x[i], end="+")
