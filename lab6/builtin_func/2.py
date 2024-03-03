# Write a Python program with builtin function that accepts a string and calculate the number of upper case letters and lower case letters

my_string = str(input("Input string: "))

lower_case = sum(1 for i in my_string if i.islower())
upper_case = sum(1 for i in my_string if i.isupper())

print("Lower case letters:", lower_case, "\nUpper case letters:", upper_case)

#done