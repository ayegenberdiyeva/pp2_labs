
# Write a Python program that matches a string that has an 'a' followed by zero or more 'b''s.

import re

pattern = ("a[b]*")

string = str(input("String: "))
x = re.search(pattern, string)

if re.search(pattern, string):
    print("Found a match")
else :
    print("Not matched")

#done