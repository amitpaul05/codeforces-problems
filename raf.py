x = [int(x) for x in input().split()]

i = 0
while x[i] > 0:
    x.remove(x[i])
    print(x)
print(x[0])
