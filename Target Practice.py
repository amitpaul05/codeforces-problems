t = int(input())
value = [i for i in range(6)]
while t:
    sum = 0
    for i in range(10):
        a = list(input())
        indexi = i+1
        if indexi > 5:
            indexi = 10 -i
        for j in range(10):
            if a[j] == "X":
                indexj = j + 1
                if indexj > 5:
                    indexj = 10 - j
                sum += value[min(indexj, indexi)]
    print(sum)
    t -= 1