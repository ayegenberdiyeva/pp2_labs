# Write a Python program to calculate the area of regular polygon.
# Input number of sides: 4
# Input the length of a side: 25
# The area of the polygon is: 625

import math

num_of_sides = int(input("Sides: "))
len_of_sides = int(input("Lengtht of side: "))
apothem = len_of_sides*2*math.tan(180*num_of_sides)

area = float(num_of_sides*len_of_sides*apothem/2)
print("Area:", area)

#formula