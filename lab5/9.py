
# Write a Python program to insert spaces between words starting with capital letters.

import re

pattern = ('[A-Z][^A-Z]*')

string = str(input("String: "))
x = re.findall(pattern, string)

for i in x:
    print(i, end=" ")

#done