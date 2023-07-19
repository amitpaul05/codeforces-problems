t = int(input())

while t:
    n = int(input())
    x = [int(x) for x in input().split()]
    tnum = x[0]
    cnum = x[1]
    if tnum != cnum:
        if tnum != x[2]:
            print(1)
        else:
            print(2)
    else:
        for i in range(2, len(x)):
            if x[i] != cnum:
                print(i + 1)
    t -= 1
