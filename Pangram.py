import string


n = int(input())
x = input()
i = x.lower()
y = list(i)

if n < 26:
    print("NO")
    exit()
count = 1
for letter in string.ascii_lowercase:
    count = y.count(letter)
    if count == 0:
        print("NO")
        exit()
print("YES")
