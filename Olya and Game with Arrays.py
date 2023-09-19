t = int(input())
while t:
    N = n = int(input())
    arr = []
    sec_min = []
    minimums = []
    while n:
        m = int(input())
        a = [int(x) for x in input().split()]
        if N == 1:
            print(min(a))
            break
        a.sort()
        arr.append(a)
        sec_min.append(a[1])
        minimums.append(a[0])
        n -= 1
    if arr:
        # print(arr, sec_min, min(sec_min), sec_min.index(min(sec_min)))

        # minimums.remove(minimums[sec_min.index(min(sec_min)])

        z = (sum(sec_min) - min(sec_min)) + min(minimums)

        print(z)
    t -= 1