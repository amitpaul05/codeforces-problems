from math import factorial

t = int(input())
check = (int(input()) for i in range(t))
for i in check:
    x = i-1
    num = factorial(i)+factorial(i-1)
    while x >= 2:
        if (factorial(x)+factorial(x-1)) % i == 0:
            print(x)
            break
        else:
            x -= 1
