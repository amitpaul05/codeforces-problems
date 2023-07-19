n = int(input())
x = []
sumx, sumy, sumz = 0, 0, 0
while n:
    indices = [int(x) for x in input().split()]
    sumx += indices[0]
    sumy += indices[1]
    sumz += indices[2]
    n -= 1

if sumx == 0 and sumy == 0 and sumz == 0:
    print("YES")
else:
    print("NO")
