import math

n = int(input())

s = [int(x) for x in input().split()]
count = s.count(4)
count1 = s.count(1)
count2 = s.count(2)
count3 = s.count(3)

if count1 > count3:
    count1 = count1 - count3
    count = count + count3
else:
    count1 = 0
    count = count + count3
temp = (count2 * 2) + (count1 * 1)
# print(math.ceil(temp/4), temp/4, count)
print(math.ceil(count+(temp/4)))
