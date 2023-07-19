n = int(input())
for i in range(1, n + 1):
    if i == n:
        if (i % 2) == 1:
            print("I hate", end=' it')
        else:
            print("I love", end=' it')
    elif (i % 2) == 1:
        print("I hate", end=' that ')
    else:
        print("I love", end=' that ')
