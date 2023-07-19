t = int(input())

while t:
    n = [int(x) for x in input().split()]
    for i in range(2):
        if n[i] < 0:
            n[i] = -n[i]
    if n[0] > n[1]:
        print((n[0]*2)-1)
    elif n[1] > n[0]:
        print((n[1]*2)-1)
    else:
        print(n[0]*2)
    t -= 1
