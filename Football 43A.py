import collections
n = int(input())
x = [input() for i in range(n)]


s = collections.Counter(x)
max = max(s.values())
team = filter(lambda x: s[x] == max, s)
for i in team:
    print(i)
