n = int(input())

x = [100, 20, 10, 5, 1]
temp = 0
count = 0
for i in x:
    if n >= i:
        temp = n % i
        c = n//i
        count += c
        if temp == 0:
            print(count)
            exit()
        else:
            n = temp
