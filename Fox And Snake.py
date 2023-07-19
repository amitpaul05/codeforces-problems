r, c = [int(x) for x in input().split()]

def odd():
    for j in range(c):
        print("#",end="")
    print()

def even(i):
    if i % 4 == 0:
        print("#", end="")
        for j in range(c-1):
            print(".", end="")
    else:
        for j in range(c-1):
            print(".", end="")
        print("#", end="")
    print()

for i in range(1,r+1):
    if i%2 == 0:
        even(i)
    else:
        odd()