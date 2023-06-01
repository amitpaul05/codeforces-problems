t = int(input())
while t:
    n = int(input())
    if n == 4:
        print(26)
    else:
        num = n - 4
        res = ((num * 11) + ((num - 1) * 2 * (num - 1))) + 26
        print(res)
    t -= 1
