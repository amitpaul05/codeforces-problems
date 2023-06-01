n = int(input())

weight = [int(x) for x in input().split()]
profit = [int(x) for x in input().split()]

res = []
temp = []

for i in range(n):
    res.append(profit[i]/weight[i])
    temp.append(profit[i]/weight[i])

temp.sort(reverse=True)
print(res)
sum = 0
optimum = 0
i = 0
while sum <= 20:
    index = res.index(temp[i])
    print(index)
    sum = sum + weight[index]
    if sum <= 20:
        optimum += profit[index]
        print(profit[index])
    i += 1

print(optimum)
