t = int(input())

while t:
    n, m = [int(x) for x in input().split()]
    x = [int(x) for x in input().split()]
    x.sort(reverse=True)
    c1 = x.count(-1)
    c2 = x.count(-2)
    count = 0
    if x[0] > 0:
        if c1 == 0 and c2 == 0:
            temp = 0
            for i in x:
                if m >= i != temp:
                    count += 1
                    temp = i
        else:
            if x[0] > m:
                i = 0
                while x[i] > m:
                    x.remove(x[i])
                    i += 1
            temp = m - x[0]
            count = temp
            c2 -= count
            i = 0
            while x[i] > 0:
                count += 1
                temp = x[i]-x[i+1]
                if c2 > 0:
                    count += 1
                    c2 -= 1
                else:
                    count += 1
                    c1 -= 1
                i += 1
            temp = x[i-1]-1
            if c1 < temp:
                count += c1
            else:
                count += temp
    else:
        count = c1
        if c1 < c2:
            count = c2
        if count > m:
            count = m
    print(count)
    t -= 1

    '''if c1 == 0 and c2 == 0:
        temp = 0
        for i in x:
            if m >= i != temp:
                count += 1
                #print(count)
                temp = i
    elif c1 == 0 or c2 == 0:
        count = c1
        #print(count)
        if c2 > c1:
            count = c2
        temp = 0
        i = 0
        while x[i] > 0:
            if m >= x[i] != temp:
                count += 1
                #print(count)
                temp = x[i]
            i += 1
    else:
        count = 1
        temp1 = m - x[0]
        temp2 = x[0] - 1
        if temp1 < c2:
            count = count + temp1
        else:
            count = count + c2
        if temp2 < c1:
            count = count + temp2
        else:
            count = count + c1
    print(count)
    t -= 1'''
