
# Write a Python program to replace all occurrences of space, comma, or dot with a colon.

import re

pattern = ("[ .,]")

string = str(input("String: "))

x = re.sub(pattern, ":", string)

print(x)

#done