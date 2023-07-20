n = int(input())
f = 0

if n % 2 == 0:
    f = n / 2
else:
    f = -(n / 2)-1
print(int(f))
'''for i in range(1, n + 1):
    if i % 2 == 0:
        f = f + i
    else:
        f = f - i'''
# f = f + (math.pow(-1, i) * i)
