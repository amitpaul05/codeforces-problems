count = 0
s = 0
t = int(input())
for i in range(t):
    n = int(input())
    l = [int(a) for a in input().split()]
    for j in range(n):
        k = j-1
        while k >= 0:
            s += l[k]
            print(j, k)
            k -= 1
        print(s)
        if s == l[j]:
            print("YES")
            l.sort(reverse=True)
            print(l)
            count = 1
            s = 0
            break
    if count == 0:
        print("NO")
    count = 0
    s = 0
