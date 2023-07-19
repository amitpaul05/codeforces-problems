def printDivisors(n):
    while n > 1:
        if n%2 == 0:
            n = n/2
        else:
            return 2
    return 1

    # can also be done by__

    '''if n & (n - 1) != 0:
        return 2
    else:
        return 1'''


t = int(input())
while t:
    n = int(input())
    if n % 2 == 0 and n > 4:
        if printDivisors(n) != 1:
            print("YES")
        else:
            print("NO")
    elif n % 2 != 0:
        print("yes")
    else:
        print("NO")
    t -= 1
