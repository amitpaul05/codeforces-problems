n, k = [int(x) for x in input().split()]

x = [int(x) for x in input().split()]
x.sort()
if n == 1 and x[0] != 1:
    print(x[0]-1)
elif x[k-1] == x[k]:
    print(-1)
else:
    print(x[k-1])
