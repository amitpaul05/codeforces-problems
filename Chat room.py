s = input()
if s.count('h') < 1 or s.count('e') < 1:
    print("NO")
    exit()
ind = s.rindex('h')
if s.index('e') < ind:
    ind = s.index('h')

result = 'h'
count = 0
for i in range(ind + 1, len(s)):
    if (s[i] == 'e' and result[-1] == 'h') or (s[i] == 'o' and result[-1] == 'l' and result.count('l') == 2):
        result = result + s[i]
    elif s[i] == 'l':
        if result.count('l') < 2 and (result[-1] == 'l' or result[-1] == 'e'):
            result += s[i]
        else:
            continue
if result == "hello":
    print("YES")
else:
    print("NO")
