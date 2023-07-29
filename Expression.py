a = int(input())
b = int(input())
c = int(input())
ans = 0
if min(a, b, c) == 1:
    if a == 1 and c == 1:
        ans = a + b + c
    elif c == 1:
        ans = (b + c) * a
    elif b == 1:
        ans = (b + min(a, c)) * max(a, c)
    else:
        ans = (a + b) * c
else:
    ans = a * b * c

print(ans)
