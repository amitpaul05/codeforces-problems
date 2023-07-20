n = int(input())
x = [int(x) for x in input().split()]
y = [int(y) for y in input().split()]
b = []
c = []
count1, count2 = 0, 0
res = 0
for i in range(1, x[0] + 1):
    b.append(x[i])
for j in range(1, y[0] + 1):
    c.append(y[j])
for k in range(1, n+1):
    res = 0
    count1 = b.count(k)
    count2 = c.count(k)
    if count2 == 0 and count1 == 0:
        print('Oh, my keyboard!')
        exit()
    else:
        res = 1

if res == 1:
    print("I become the guy.")
