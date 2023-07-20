def isWUB(temp):
    if temp == "WUB":
        return 0
    else:
        return 1


p = input()
res = ""
if len(p) < 3:
    print(p)
    exit()
i = 0
j = i + 2
count = 0
while j < len(p):
    temp = ""
    for a in range(i, j+1):
        temp = temp + p[a]
    m = isWUB(temp)
    if m == 0:
        if res != "" and count == 0 and j < len(p)-1:
            res = res + " "
        i = j + 1
        j = i + 2
        count = 1
    else:
        count = 0
        res = res + p[i]
        i += 1
        j += 1
        if j == len(p):
            break
d = len(p) -1
c = d - 2
temp = ""
for a in range(c, d + 1):
    temp += p[a]
if isWUB(temp) != 0:
    while i != len(p):
        res = res + p[i]
        i += 1
print(res)
