
# Write a Python program to find the sequences of one upper case letter followed by lower case letters.

import re

pattern = ("[A-Z][a-z]")

string = str(input("String: "))

if re.search(pattern, string):
    print("Found a match")
else :
    print("Not matched")

#done