n, k = [int(x) for x in input().split()]

x = [int(x) for x in input().split()]

result = sum([x[i] for i in range(k)])
print(result)
temp = result
index = 1
for i in range(k, n):
    temp = (temp + x[i]) - x[i-k]
    if result > temp:
        result = temp
        index = (i - k)+2
print(index)