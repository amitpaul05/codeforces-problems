t = int(input())
while t != 0:
    a, b = [int(a) for a in input().split()]
    if a == b:
        print('0')
    elif a > b:
        if (a - b) % 2 == 0:
            print('1')
        else:
            print('2')
    elif a < b:
        if (b - a) % 2 == 1:
            print("1")
        else:
            print("2")
    t -= 1
