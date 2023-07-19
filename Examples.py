for n in range(2, 5):
    print(n)

x = int(input("Enter x : "))
num = x
fact = 1
while num != 1:
    fact = fact * num
    num -= 1
print(f"Factorial of {x} is {fact}")

count = 0

for i in range(2, int(x / 2)):
    if x % i == 0:
        count = 1
        break

if count == 0:
    print(x, "is prime.")
else:
    print(x, "is not prime")

if x % 2 == 0:
    print(x, "is an odd number")
else:
    print(x, "is Even")

y = int(input("Enter y : "))

print(f"The sum is {x + y}")

n = int(input("n = "))
a = 1
b = 1
print(a)
print(b)

for i in range(2, n):
    fibo = a + b
    a = b
    b = fibo
    print(fibo)
