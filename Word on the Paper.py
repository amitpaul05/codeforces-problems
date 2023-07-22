


t = int(input())

while t:
    mat = [[x for x in input()] for y in range(8)]
    index = 0
    for i in mat:
        if i.count('.') == 7:
            index = mat.index(i)
            break
    ind = 0
    for i in mat[index]:
        if i != '.':
            ind = mat[index].index(i)
    result = ''
    while index < 8:
        if mat[index][ind] == '.':
            break
        result = result + mat[index][ind]
        index += 1
    print(result)
    t -= 1
