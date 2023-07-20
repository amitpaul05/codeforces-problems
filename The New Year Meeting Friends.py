x = [int(x) for x in input().split()]

x.sort(reverse=True)

a = x[0] - x[1]
b = x[0] - x[2]
c = x[0] - x[3]

print(a, b, c)



