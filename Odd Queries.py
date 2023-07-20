t = int(input())

while t:
    n, q = [int(x) for x in input().split()]
    a = [int(x) for x in input().split()]
    while q:
        sum = 0
        l, r, k = [int(x) for x in input().split()]
        i = 0
        while i != n:
            if i == l-1:
                j = i
                while j != r:
                    sum = sum + k
                    print(f"==> {sum},{k} ", end=" ")
                    j += 1
                    i = j
            if r == n:
                break
            else:
                sum = sum + a[i]
            print(sum, end=" ")
            i += 1
        if sum % 2 != 0:
            print("YES")
        else:
            print("NO ", sum)
        q -= 1
    t -= 1

