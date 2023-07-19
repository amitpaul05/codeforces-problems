n = int(input())
x = [int(x) for x in input().split()]
x.sort(reverse=True)

sum = sum(x)

temp = sum / 2
res = 0
count = 0
for i in x:
    res = res + i
    count += 1
    if res > temp:
        break
print(count)