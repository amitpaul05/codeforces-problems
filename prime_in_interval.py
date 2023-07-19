import prime

a = int(input("Enter the interval\nFrom : "))
b = int(input("To : "))

for i in range(a, b):
    value = prime.Prime(i)
    if value == 0:
        print(i)
