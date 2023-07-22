t = int(input())
while t:
    n, k = [int(x) for x in input().split()]
    x = [int(x) for x in input().split()]
    x.sort()
    count = []
    c = 1
    if n == 1:
        count.append(1)
    else:
        for i in range(1, n):
            dif = x[i] - x[i - 1]
            if dif <= k:
                c += 1
            else:
                count.append(c)
                c = 1
            if i == n-1:
                count.append(c)
    print(n - max(count))
    t -= 1