arr = "codeforces"
t = int(input())
while t:
    c = input()
    count = arr.count(c)
    if count > 0:
        print("YES")
    else:
        print("NO")
    t -= 1
