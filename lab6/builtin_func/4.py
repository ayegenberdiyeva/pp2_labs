# Write a Python program that invoke square root function after specific milliseconds.
# Sample Input:
# 25100
# 2123
# Sample Output:
# Square root of 25100 after 2123 miliseconds is 158.42979517754858

from time import sleep

square = int(input("Input square: "))
sleeping_time = int(input("Input sleeping time: "))

sleep(sleeping_time/1000)

sqrt =  square ** 0.5

print(f"Square root of {square} after {sleeping_time} miliseconds is {sqrt}")

#done