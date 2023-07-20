t = int(input())

while t:
    l = int(input())
    length, j = l, l
    s = input()
    for i in range(j//2):
        l = -(i+1)
        if (int(s[i]) == 0 and int(s[l]) == 1) or (int(s[i]) == 1 and int(s[l]) == 0):
            length = length - 2
        else:
            break
    print(length)
    t -= 1
