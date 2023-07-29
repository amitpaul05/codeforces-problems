t = int(input())

while t:
    count = 0
    n, m, k, h = [int(x) for x in input().split()]
    H = [int(x) for x in input().split()]
    for i in H:
        height = abs(h-i)
        x = height // k
        if height % k == 0 and x <= m - 1 and i != h:
            count += 1
    print(count)
    t -= 1