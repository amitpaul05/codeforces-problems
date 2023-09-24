t = int(input())
while t:
    n = int(input())
    a = input()
    start = []
    count = 0
    for i in a:
        if i == '(':
            start.append(i)
        else:
            if start:
                start.pop(-1)
            else:
                count += 1
    print(count)
    t -= 1


