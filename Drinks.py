import statistics
n = int(input())

x = [int(x) for x in input().split()]
print(statistics.mean(x))
ans = sum(x)/n
print(ans)
