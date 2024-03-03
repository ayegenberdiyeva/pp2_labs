# Write a Python program to write a list to a file.

myList = [i for i in input().split()]

with open(
    "/Users/aminayegenberdiyeva/Desktop/test/text.txt",
    "w",
) as file:
    for i in myList:
        file.writelines(i + "\n")