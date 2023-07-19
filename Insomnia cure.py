k = int(input())
l = int(input())
m = int(input())
n = int(input())
d = int(input())
count = 0
for i in range(1, d + 1):
    if i % k and i % l and i % m and i % n != 0:
        count += 1
print(d - count)
