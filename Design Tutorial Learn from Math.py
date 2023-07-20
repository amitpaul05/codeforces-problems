def iscomp(n):
    comp = 0
    for j in range(2, n):
        if n % j == 0:
            comp = 1
            break
    return comp


num1 = 0
num2 = 0

n = int(input())
for i in range(2, (n//2)+1):
    if iscomp(i) == 1:
        num1 = i
        num2 = n - num1
        if iscomp(num2) == 1:
            print(num1, num2)
            exit()

