a, b = [int(x) for x in input().split()]
rem = a % b
temp = a // b
ans = temp + rem
count = a

while temp >= 1:
    count += temp
    a = ans
    rem = a % b
    temp = a // b
    ans = temp + rem

print(count)