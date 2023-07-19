t = int(input())

while t:
    b = input()
    a = ""
    if len(b) == 2:
        a = b
    else:
        j = 2
        for i in range(len(b)):
            if i == j:
                j += 2
                continue
            else:
                a = a + b[i]
    print(a)
    t -= 1
