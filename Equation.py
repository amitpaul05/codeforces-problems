# cmath for complex solves

import cmath

# x, y, z = int(input("Enter x = ")), int(input("Enter y = ")), int(input("Enter z = "))

a = int(input())
b = int(input())
c = int(input())

d = cmath.sqrt(b ** 2 - 4 * a * c)

solve1 = ((- b) + d) / 2 * a
solve2 = ((- b) - d) / 2 * a

print(f"The solves of the equation is {solve1} & {solve2}")
