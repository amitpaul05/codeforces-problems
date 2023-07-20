a = input()
b = input()
length = len(a)
res = ''

for i in range(length):
    s = int(a[i]) + int(b[i])
    if s == 2:
        s = 0
    res = res + str(s)
print(res)