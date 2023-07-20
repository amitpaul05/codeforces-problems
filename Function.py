import math


def fibo(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibo(n - 1) + fibo(n - 2)


for i in range(1, 11):
    print(fibo(i))

add = lambda x: print(math.pow(x, 2))
add(5)
