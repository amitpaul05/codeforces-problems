# count = 0


def Prime(n):
    count = 0
    for i in range(2, n):
        if n % i == 0:
            count = 1
            break

    if count == 0:
        return 0
    else:
        return 1
