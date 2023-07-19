n = int(input())
x = [int(x) for x in input().split()]
count = 0
case = 0
i = 0
while i != (n - 1):
    if x[i] < 0:
        while x[i] < 0:
            count += 1
            i += 1
    count = count - x[i]
    case = case + count
    i += 1
