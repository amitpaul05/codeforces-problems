t = int(input())
while t:
    count = 0
    n = int(input())
    x = [int(x) for x in input().split()]
    x.sort()
    if n == 1:
        print("YES")
    else:
        for i in range(n-1):
            j = i + 1
            if x[j] - x[i] > 1:
                print("NO")
                count = 0
                break
            else:
                count = 1
        if count == 1:
            print("YES")
    t -= 1