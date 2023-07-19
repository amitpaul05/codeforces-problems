t = int(input())
x = []
digits = [0 for i in range(10)]

freeq = "abcdefghijklmnopqrstuvwxyz"
while t:
    s = input()
    for i in freeq:
        count = s.count(i)
        x.append(count)
    # zero
    digits[0] = x[25]
    x[4] -= x[25]
    x[17] -= x[25]
    x[14] -= x[25]

    # two
    digits[2] = x[22]
    x[19] -= x[22]
    x[14] -= x[22]

    # four
    digits[4] = x[20]
    x[5] -= x[20]
    x[14] -= x[20]
    x[17] -= x[20]

    # six
    digits[6] = x[23]
    x[18] -= x[23]
    x[8] -= x[23]

    # eight
    digits[8] = x[6]
    x[4] -= x[6]
    x[8] -= x[6]
    x[7] -= x[6]
    x[19] -= x[6]

    # one
    digits[1] = x[14]
    x[13] -= x[14]
    x[4] -= x[14]

    # three
    digits[3] = x[19]
    x[7] -= x[19]
    x[17] -= x[19]
    x[4] -= x[19]
    x[4] -= x[19]

    # five
    digits[5] = x[5]
    x[8] -= x[5]
    x[21] -= x[5]
    x[4] -= x[5]

    # seven
    digits[7] = x[18]
    x[4] -= x[18]
    x[21] -= x[18]
    x[4] -= x[18]
    x[13] -= x[18]

    # nine
    digits[9] = x[8]
    x[13] -= x[20]
    x[13] -= x[20]
    x[4] -= x[20]

    for i in range(1, 10):
        if digits[i] > 0:
            print(i, end="")
            digits[i] -= 1
            break
    for i in range(10):
        if digits[i] > 0:
            for j in range(digits[i]):
                print(i, end="")

    t -= 1
