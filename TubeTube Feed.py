t = int(input())

while t:
    count = 0
    n, q = [int(x) for x in input().split()]
    a = [int(x) for x in input().split()]
    b = [int(x) for x in input().split()]
    c = []
    minimum = a[0]
    for i in range(1, n):
        if a[i] < minimum:
            minimum = a[i]
    if minimum > q:
        print(-1)
    else:
        for i in range(n):
            c.append(b[i])
        c.sort(reverse=True)
        for i in c:
            index = b.index(i)
            time = q - index
            if time >= a[index]:
                print(index + 1)
                count = 0
                break
            else:
                count = 1
        if count == 1:
            print(-1)
    t -= 1
