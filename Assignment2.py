import math
import cmath

# Area of Triangle
print("\t\tBasic math formulas")
print("#" * 50)
print(" " * 16 + "Area of Triangle")
print("-" * 50)

base = float(input("Enter Base:"))
height = float(input("Enter Height:"))

area_triangle = round(0.5 * base * height, 2)

print("The area is " + str(area_triangle))

# Area of Rectangle
print("-" * 50)
print(" " * 16 + "Area of Rectangle")
print("-" * 50)

length = float(input("Enter Length:"))
width = float(input("Enter Width:"))

area_rectangle = round(length * width, 2)

print("The area is " + str(area_rectangle))

# The Longest Size of Right Triangle
print("-" * 50)
print(" " * 8 + "The Longest Size of Right Triangle")
print("-" * 50)

length_a = float(input("Enter length of the 1st size:"))
length_b = float(input("Enter length of the 2st size:"))

length_c = round(math.sqrt(length_a**2 + length_b**2), 2)

print("The length of the longest size is", length_c)

# The Solution of Quadratic Formula
print("-" * 50)
print(" " * 8 + "The Solution of Quadratic Formula")
print("-" * 50)

c_val = float(input('Enter Constant("c"):'))
b_val = float(input('Enter Coefficient of Linear Term("b"):'))
a_val = float(input('Enter Coefficient of Quadratic Term("a"):'))

discriminant = b_val**2 - 4 * a_val * c_val

if discriminant >= 0:
    sol_1 = (-b_val + math.sqrt(discriminant)) / (2 * a_val)
    sol_2 = (-b_val - math.sqrt(discriminant)) / (2 * a_val)
else:
    sol_1 = (-b_val + cmath.sqrt(discriminant)) / (2 * a_val)
    sol_2 = (-b_val - cmath.sqrt(discriminant)) / (2 * a_val)

print("The 1st solution is x =", str(sol_1))
print("The 2st solution is x =", str(sol_2))

# Distance of 2 points
print("-" * 50)
print(" " * 16 + "Distance of 2 points")
print("-" * 50)

x1 = float(input("Enter x of the 1st point:"))
y1 = float(input("Enter y of the 1st point:"))
x2 = float(input("Enter x of the 2nd point:"))
y2 = float(input("Enter y of the 2nd point:"))

distance = round(math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2), 2)

print("The distance is", str(distance))

print("-" * 50)
