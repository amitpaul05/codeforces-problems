t = int(input())
while t:
    count = 0
    n = int(input())
    x = [int(x) for x in input().split()]
    x.sort()
    maximum = max(x)
    minimum = min(x)
    if x.count(x[0]) == n:
        count = 1
    else:
        s_array = [i for i in range(minimum, maximum+1)]
        if s_array == x:
            count = 1
        for i in x:
            if x.count(i) > 1:
                count = 0
    if count == 1:
        print("YES")
    else:
        print("NO")
    t -= 1