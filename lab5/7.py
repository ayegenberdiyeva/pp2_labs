
# Write a python program to convert snake case string to camel case string.

import re

pattern = ("[_]")

string = str(input("String: "))
x = re.split(pattern, string)

for i in x:
    print(i.capitalize(), end='')

#done