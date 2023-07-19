n, k = [int(x) for x in input().split()]

minutes = 240 - k

time = 0
count = 0
for i in range(1, n+1):
    time = time + (i*5)
    if time > minutes:
        break
    count += 1
    if minutes -time < 5:
        break
print(count)