for i in range(6):
    for j in range(i):
        print(j, end=' ')
    print()

numbers = [int(input(f"Enter item {x}: ")) for x in range(10)]
numbers.sort()

sum = 0
for i in numbers:
    sum += i

print(sum)
