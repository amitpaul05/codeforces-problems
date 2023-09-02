n = int(input())
x = [int(x) for x in input().split()]
x.sort()
q = int(input())
m = [int(input()) for i in range(q)]
pre_sum = [x.]

for i in m:
    if i < x[0]:
        mid = 0
    elif i >= x[len(x)-1]:
        mid = len(x)
    else:
        low = 0
        high = len(x) - 1
        while low < high:
            mid = (low + high) // 2
            if x[mid] == i:
                mid = mid + 1
                break
            elif i > x[mid]:
                low = mid + 1
            else:
                high = mid - 1
        # print(low, high, mid, i, x[mid])
        if i > x[high]:
            mid = high + 1
        elif i > x[mid]:
            mid = mid + 1
    print(mid)
