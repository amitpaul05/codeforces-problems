s = input()
count = 0
if len(s) == 1:
    if s.isupper():
        print(s.lower())
        exit()
    else:
        print(s.upper())
        exit()
if s.islower():
    print(s)
    exit()
elif s.isupper():
    print(s.lower())
    exit()

for i in range(1, len(s)):
    if s[i].isupper():
        count = 1
    else:
        count = 0
        break
if count == 0:
    print(s)
else:
    print(s.capitalize())