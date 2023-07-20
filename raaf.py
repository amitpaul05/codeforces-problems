a = input()
b = input()
c = input()
count1 = 0
count2 = 0
x = a + b
list1 = list(x)
list2 = list(c)

for i in x:
    count1 = list1.count(i)
    count2 = list2.count(i)
    if count1 != count2 or len(x) != len(c):
        print("NO")
        exit()
print("YES")
