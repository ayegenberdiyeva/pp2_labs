# Write a Python program to test whether a given path exists or not. If the path exist find the filename and directory portion of the given path.

import os

def test_path(path):
    if os.path.exists(path):

        directory, filename = os.path.split(path)
        return True, directory, filename
    else:
        return False, None, None

path = str(input("Input directory to test: "))

exists, directory, filename = test_path(path)

if exists:
    print(f"The path '{path}' exists.")
    print(f"Directory: {directory}")
    print(f"Filename: {filename}")
else:
    print(f"The path '{path}' does not exist.")
