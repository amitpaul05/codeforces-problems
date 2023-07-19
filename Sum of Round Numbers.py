t = int(input())
while t:
    count = 0
    a = 0
    x = []
    n = int(input())
    temp = n
    temp1 = n
    i = 10
    while temp > 0:
        temp = temp % i
        if temp != 0:
            x.append(temp)
            temp = temp1 - temp
            temp1 = temp
        else:
            count = 0
            a = 0
            while temp1 > 10:
                count = count + 1
                temp1 = temp1 // 10
                temp = temp1 % 10
                if temp != 0:
                    temp = temp * (10**count)
                    temp1 = temp1 * (10**count)
                    x.append(temp)
                    a = 0
                    break
                else:
                    a = 1
            if a == 1:
                break
        if a == 1:
            x.append(temp1)
            break
        elif count == 0:
            i = i * 10
        else:
            i = 10 ** count
    print(len(x))
    for j in x:
        print(j, end=" ")
    print()
    t -= 1