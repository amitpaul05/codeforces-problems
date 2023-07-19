def maxprint(count, a):
    j = 0
    for k in range(a):
        j += 1
        print(j, end=" ")
    for k in range(count):
        j -= 1
        print(j, end=" ")
    print()


def minprint(count, n):
    for k in range(count):
        print("1 0", end=" ")
    j = 0
    a = n - count*2
    for k in range(a):
        j += 1
        print(j, end=" ")
    print()


t = int(input())
while t:
    n = int(input())
    x = [int(x) for x in input().split()]
    count = 0
    for i in x:
        if i < 0:
            count += 1
    a = n - count
    maxprint(count, a)
    minprint(count, n)
    t -= 1
