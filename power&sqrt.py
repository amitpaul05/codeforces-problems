import math
import cmath

print(math.lcm(5, 6, 4))
a = int(input("Enter the number : "))

print(f"The Square root of {a} is {math.sqrt(a)}")

b = int(input("to the power : "))
print(f"{a} to the power {b} is {math.pow(a, b)}")

a = complex(input("Enter a complex number : "))

print(type(a))

print(f"The square root of {a} is {cmath.sqrt(a)}")
