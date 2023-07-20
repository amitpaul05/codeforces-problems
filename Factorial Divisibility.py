import math

n, x = [int(x) for x in input().split()]
res = 0
y = [int(y) for y in input().split()]
for i in y:
    res += math.factorial(i)
if res % math.factorial(x) == 0:
    print("YES")
else:
    print("NO")
