
c, d = 0, 0

t = int(input())
while t:
    x = 0
    y = 0
    count = 0
    n = int(input())
    s = input()
    for i in s:
        if i == "U":
            y = y+1
        elif i == "D":
            y -= 1
        elif i == "L":
            x -= 1
        elif i == "R":
            x += 1
        c = x
        d = y
        if x == 1 and y == 1:
            count = 1
            break
    if count == 1:
        print("YES")
    else:
        print("NO")
    t -= 1
