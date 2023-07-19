n = int(input())
x = [int(x) for x in input().split()]
max = x[0]
min = x[0]
count = 0

for i in range(1,n):
    if x[i] > max:
        count += 1
        max = x[i]
    elif x[i] < min:
        count += 1
        min = x[i]
print(count)