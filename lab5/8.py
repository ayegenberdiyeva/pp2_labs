
# Write a Python program to split a string at uppercase letters.

import re

pattern = ('[A-Z][^A-Z]*')

string = str(input("String: "))
x = re.findall(pattern, string)

print(x)

#done