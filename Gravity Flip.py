n = int(input())

x = [int(x) for x in input().split()]

x.sort()
for i in x:
    print(i, end=" ")
