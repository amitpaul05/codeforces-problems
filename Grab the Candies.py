t = int(input())

while t:
    Mihai = 0
    Bianca = 0
    n = int(input())
    a = [int(x) for x in input().split()]
    for i in a:
        if i % 2 == 0:
            Mihai += i
        else:
            Bianca += i
    if Mihai > Bianca:
        print("YES")
    else:
        print("NO")
    t -= 1
