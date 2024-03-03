# Write a Python program to delete file by specified path. Before deleting check for access and whether a given path exists or not.

import os
import sys

if len(sys.argv) < 2:
    print("Write arguments!")
    sys.exit()
if not os.path.exists(sys.argv[1]):
    print("Path doesn't exist")
    sys.exit()

try:
    os.remove(sys.argv[1])
    print("File successfully deleted")
except PermissionError:
    print("You don't have permission to delete file")
