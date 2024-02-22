
# Write a Python program that matches a string that has an 'a' followed by two to three 'b'.

import re

pattern = ("a[b]{2,3}")

string = str(input("String: "))
x = re.search(pattern, string)

if re.search(pattern, string):
    print("Found a match")
else :
    print("Not matched")

#done