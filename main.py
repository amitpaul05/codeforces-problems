PI = 3.14


def sum(a=5, b=3):
    print(f"The sum is {a + b}")


sum(2, 3)
sum(b=4)
sum()


def add(*x):
    result = 0
    print("The sum of", end=" ")
    for num in x:
        result += num
        print(num, end=", ")
    print(f"is : {result}")


add(4, 5, 7, 3)
add(4, 8, 15, 5, 25, 36, 48, 51, 4)
add(7, 9)

# def print_hi(name):
# Use a breakpoint in the code line below to debug your script.
# print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
# if __name__ == '__main__':
# print_hi('PyCharm')
