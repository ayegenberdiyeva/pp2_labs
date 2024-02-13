# Write a Python program to calculate the area of a trapezoid.
# Height: 5
# Base, first value: 5
# Base, second value: 6
# Expected Output: 27.5

import math

height = int(input("Height: "))
base_1 = int(input("First Base: "))
base_2 = int(input("Second Base: "))

area = float((base_1+base_2)*height /2)

print("Area:", area)

#done