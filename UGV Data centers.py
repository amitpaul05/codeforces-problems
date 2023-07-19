N = int(input())
input()
q = 1
while N:
    N1 = []
    N2 = []
    W = []
    # n, m, s, t = [int(x) for x in input().split()]
    n = [int(x) for x in input().split()]
    sub = n[0] - n[1]
    while n[1]:
        n1, n2, w = [int(x) for x in input().split()]
        N1.append(n1)
        N2.append(n2)
        W.append(w)
        n[1] -= 1
    if sub > 1:
        print(f"Case #{q}: unreachable")
    elif n[0] == 2 and n[1] <= 2:
        W.sort()
        print(f"Case #{q}:", W[0])
    else:
        ans = 0
        if sub == 1:
            ans = sum(W)
        else:
            W.sort()
            length = len(W)
            ans = sum(W) - W[length-1]
        print(f"Case #{q}:", ans)
    N -= 1
    q += 1
    input()
