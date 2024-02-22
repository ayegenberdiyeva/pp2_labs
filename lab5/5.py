
# Write a Python program that matches a string that has an 'a' followed by anything, ending in 'b'.

import re

pattern = (r"[a][\w]+[b]\b")

string = str(input("String: "))
x = re.search(pattern, string)

if re.search(pattern, string):
    print("Found a match")
else :
    print("Not matched")

#done