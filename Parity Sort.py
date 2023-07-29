t = int(input())

while t:
    count = 1
    odd = []
    odd_ind = []
    even = []
    n = int(input())
    x = [int(x) for x in input().split()]
    for i in x:
        if i % 2 != 0:
            odd.append(i)
            odd_ind.append(x.index(i))
        else:
            even.append(i)
    odd.sort()
    even.sort()
    if len(odd) == 1 or len(even) == 1:
        flag = 0
        if all(x[i] <= x[i + 1] for i in range(len(x) - 1)):
            flag = 1
        if flag:
            count = 1
        else:
            count = 0
    elif len(odd) == 1 or len(even) == 1:
        count = 1
    else:
        for i in range(len(odd) - 1):
            if odd_ind[i + 1] - odd_ind[i] > 1:
                for j in range((odd_ind[i + 1] - odd_ind[i]) - 1):
                    if odd[i] < even[j] < odd[i + 1]:
                        pass
                    else:
                        count = 0
                        break
                if count == 0:
                    break
    if count == 0:
        print("NO")
    else:
        print("Yes")
    t -= 1