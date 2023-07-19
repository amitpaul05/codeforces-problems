import math
import random

languages = ['Python', 'Swift', 'C++', 'C', 'Java', 'Rust', 'R']
del languages[2: 3]  # ['C', 'Java', 'Rust']
print(languages)
num = [4, 9, 5, 6]
num.sort()
print(num)

print("The gcd is: ", math.gcd(20, 50))

print(f"The binary value of 300 is {bin(300)}")


# convert binary to decimal
print(0b10111011)

# convert octal to decimal
print(0o17147)

# convert hexadecimal to decimal
print(0xab500)

print(random.randrange(1, 1000))
print(random.SystemRandom())

a = input("Enter a number : ")
a = complex(a)
