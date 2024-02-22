
# Write a Python program to find sequences of lowercase letters joined with a underscore.

import re

pattern = ("[a-z]([_][a-z])+")

string = str(input("String: "))
x = re.search(pattern, string)

if re.search(pattern, string):
    print("Found a match")
else :
    print("Not matched")

#done