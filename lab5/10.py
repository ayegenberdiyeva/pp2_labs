
# Write a Python program to convert a given camel case string to snake case.

import re

pattern = ('[A-Z][^A-Z]*')

string = str(input("String: "))
x = re.findall(pattern, string)

for i in range(len(x)):
    if (i == len(x)-1):
        print(x[i].lower())
        break
    print(x[i].lower(), end='_')

#done