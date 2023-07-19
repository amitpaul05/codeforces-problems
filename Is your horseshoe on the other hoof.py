a = [int(x) for x in input().split()]
j = []
count1 = 1
count = 0
for i in a:
    count1 = a.count(i)
    for l in j:
        if l == i:
            count1 = 1
    if count1 > 1:
        count1 = count1 - 1
        j.append(i)
        count += count1
print(count)
