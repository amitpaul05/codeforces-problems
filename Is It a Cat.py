t = int(input())
arr = "meow"
while t:
    j = 0
    n = int(input())
    s = input()
    s = s.lower()
    for i in range(n):
        temp = s[i]
        if temp == arr[j]:
            pass
        elif j == 3:
            while i != n:
                temp = s[i]
                if temp != 'w':
                    print("NO")
                    j = 0
                    break
                elif temp == 'w' and i == (n-1):
                    j = 3
                    break
                i += 1
        elif temp == arr[j + 1] and i > 0:
            j += 1
        else:
            print("NO")
            break
    if j == 3:
        print("YES")
    t -= 1
