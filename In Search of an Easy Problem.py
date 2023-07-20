n = int(input())

x = [int(x) for x in input().split()]
i = x.count(1)
if i == 0:
    print("EASY")
else:
    print("HARD")
