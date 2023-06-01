s = input()
x = s.lower()
a = ""
for i in x:
    if i != 'a' and i != 'e' and i != 'i' and i != 'o' and i != 'u' and i != 'y':
        a = a + (f".{i}")
print(a)