s = input()

i = 0
while i != len(s):
    count1 = 0
    count0 = 0
    temp = s[i]

    if temp == "0":
        while i < len(s) - 1 and s[i] == s[i + 1]:
            count0 += 1
            i += 1

            if count0 == 6:
                print("YES")
                exit()
    elif temp == "1":
        while i < len(s) - 1 and s[i] == s[i + 1]:
            count1 += 1
            i += 1
            if count1 == 6:
                print("YES")
                exit()
    i += 1
print("NO")