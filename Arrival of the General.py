n = int(input())

x = [int(x) for x in input().split()]

y = x.copy()
y.sort(reverse=True)
num1 = y[0]
num2 = y[n - 1]

if num1 == x[0] and num2 == x[n-1]:
    print(0)
else:
    l = x.index(num1)
    k = x.index(num2)
    if num2 == x[n-1]:
        print(l)
    else:
        count1 = x.count(num1)
        count2 = x.count(num2)

        if count2 > 1:
            for i in range(count2 - 1):
                s = k
                k = x.index(num2, s + 1, n - 1)
        o = (n - 1) - k
        if l > k:
            ans = (o + l) - 1
        else:
            ans = o + l
        print(ans)
