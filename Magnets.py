n = int(input())

x = [int(input()) for i in range(n)]
count = 0
for i in range(n-1):
    if x[i] != x[i+1]:
        count += 1
print(count+1)