t = int(input())

while t:
    n, k = [int(x) for x in input().split()]
    s = input()
    cb = 0
    count = 0
    temp = -1
    for i in range(n):
        if s[i] == 'B':
            if temp == -1:
                temp = i
            cb += 1
        if temp != -1 and ((i-temp) == k-1):
            if cb > 0:
                count += 1
                cb = 0
            temp = -1

    if cb > 0:
        count += 1
    print(count)
    t -= 1