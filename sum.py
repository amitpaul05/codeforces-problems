n = int(input("How many natural numbers : "))
sum = 0


def add(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return (add(n - 1) + 1) + n-1


for i in range(1, n + 1):
    sum = add(i)
    print(f"The sum is {sum} for {i}")
    # sum += add(i)


