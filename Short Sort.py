t = int(input())
while t:
    s = input()
    count = 0
    if s.index('a') == 0:
        count += 1
    if s.index('b') == 1:
        count += 1
    if s.index('c') == 2:
        count += 1

    if count >= 1:
        print("YES")
    else:
        print("NO")
    t -= 1