t = int(input())

while t:
    a, b, c = [int(i) for i in input().split()]
    dif = (max(a, b) - min(a, b)) / 2
    if dif % c == 0:
        moves = dif // c
    else:
        moves = (dif // c) + 1
    print(int(moves))
    t -= 1
