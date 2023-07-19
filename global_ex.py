from math import *

for i in range(0, 11, 2):
    print(i)

print(f"The value of pi is {pi}")

num = 20

print(pow(5, 2))


def outer_function():
    num = 20

    def inner_function():
        global num
        num = 25

    print("Before calling inner_function(): ", num)
    inner_function()
    print("After calling inner_function(): ", num)


outer_function()
print("Outside both function: ", num)
