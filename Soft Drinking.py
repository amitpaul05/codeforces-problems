n, k, l, c, d, p, nl, np = [int(x) for x in input().split()]

drink = k * l
t = [drink // nl, c * d, p // np]
t.sort()
res = t[0]//n
print(res)


