t = int(input())

while t:
    a, b, c = [int(x) for x in input().split()]
    plus = a + b

    if plus == c:
        print("+")
    else:
        print("-")
    t -= 1
