# Write a Python program to count the number of lines in a text file.

count = 0

with open("/Users/aminayegenberdiyeva/Desktop/test/text.txt") as file:
    for line in file:
        count += 1
print(f"The number of lines in file is: {count}")
