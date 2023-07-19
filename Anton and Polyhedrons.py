s = 0
n = int(input())
x = []
for i in range(n):
    t = input()
    x.append(t)
    if t == 'Tetrahedron':
        s += 4
    elif t == 'Cube':
        s += 6
    elif t == 'Octahedron':
        s += 8
    elif t == 'Dodecahedron':
        s += 12
    else:
        s += 20
print(s)
