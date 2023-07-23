n = int(input())
i = 4
j = 7
k = 4
l = 7
count = 0
while i <= n or j <= n or k <= n or l <= n:
    if n % i == 0 or n % j == 0 or n % k == 0 or n % l == 0:
        count = 1
    i = (i * 10) + 7
    j = (j * 10) + 4
    k = (k * 10) + 4
    l = (l * 10) + 4

if count == 1:
    print("YES")
else:
    print("NO")
