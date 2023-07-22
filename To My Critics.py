t = int(input())

while t:
    x = [int(x) for x in input().split()]
    x.sort(reverse=True)
    if x[0]+x[1] >= 10:
        print("YES")
    else:
        print("NO")
    t -= 1